import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta
import os

def load_and_clean_data(filepath):
    """Loads the CSV and performs data cleaning operations."""
    df = pd.read_csv(filepath)
    
    # Clean 1: Drop duplicated rows
    df = df.drop_duplicates()
    
    # Clean 2: Drop rows where crucial information (branch or quantity) is missing
    df = df.dropna(subset=['branch', 'quantity_kg'])
    
    # Clean 3: Remove '₹' and commas from the price column, then convert to float
    df['selling_price'] = df['selling_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
    
    # Clean 4: Convert date strings to actual datetime objects
    df['date'] = pd.to_datetime(df['date'])
    
    return df

def feature_engineering(df):
    """Creates new columns required for financial analysis."""
    df['revenue'] = df['selling_price'] * df['quantity_kg']
    df['total_cost'] = df['cost_per_kg'] * df['quantity_kg']
    df['profit'] = df['revenue'] - df['total_cost']
    
    # Map months to Indian seasons for analysis
    def get_season(month):
        if month in [3, 4, 5]: return 'Summer'
        elif month in [6, 7, 8, 9]: return 'Monsoon'
        elif month in [10, 11]: return 'Festive Season'
        else: return 'Winter'
        
    df['season'] = df['date'].dt.month.apply(get_season)
    return df

def get_best_seller(df):
    sales_by_sweet = df.groupby('sweet_name')['quantity_kg'].sum().reset_index()
    best_seller = sales_by_sweet.loc[sales_by_sweet['quantity_kg'].idxmax()]
    return best_seller['sweet_name'], best_seller['quantity_kg']

def get_branch_profits(df):
    profits = df.groupby('branch')['profit'].sum().reset_index()
    profits = profits.sort_values(by='profit', ascending=False)
    return profits

def get_busiest_season(df):
    season_revenue = df.groupby('season')['revenue'].sum().reset_index()
    busiest = season_revenue.loc[season_revenue['revenue'].idxmax()]
    return busiest['season'], busiest['revenue']

def plot_branch_profits(df):
    branch_profits = get_branch_profits(df)
    plt.figure(figsize=(8, 5))
    plt.bar(branch_profits['branch'], branch_profits['profit'], color=['#ff9999', '#66b3ff', '#99ff99'])
    plt.title('Total Profit by Branch', fontsize=14)
    plt.xlabel('Branch')
    plt.ylabel('Profit (₹)')
    # Format Y-axis to show regular numbers instead of scientific notation
    plt.ticklabel_format(style='plain', axis='y')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_sweet_sales(df):
    sales_by_sweet = df.groupby('sweet_name')['quantity_kg'].sum().sort_values(ascending=True)
    plt.figure(figsize=(10, 6))
    sales_by_sweet.plot(kind='barh', color='#fdb462')
    plt.title('Total Quantity Sold by Sweet', fontsize=14)
    plt.xlabel('Total Kilograms Sold')
    plt.ylabel('Sweet Name')
    plt.tight_layout()
    plt.show()
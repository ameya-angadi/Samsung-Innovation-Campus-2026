def partition_array(numbers):
    
    pivot = numbers[-1]     # Assign last element as reference element

    i = 0       # To parse through each element
    j = 0       # To know/find the index of pivot element


    for i in range(len(numbers)-1):
        if numbers[i]<pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # print(numbers) # Uncomment to see step wise changes to list data
            j += 1
    numbers[-1], numbers[j] = numbers[j], numbers[-1]
    return numbers

def partition_array_reccursive(numbers, low, high):
 
    pivot = numbers[high]     # Assign last element as reference element

    i = low       # To parse through each element
    j = low       # To know/find the index of pivot element


    for i in range(low, high):
        if numbers[i]<pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # print(numbers) # Uncomment to see step wise changes to list data
            j += 1
    numbers[high], numbers[j] = numbers[j], numbers[high]
    return j
import bubble_sort as bs
import bubble_sort_optimized as bs_opt
import sys

input_list = []

print(f'User given elements are: ')
for i in range(1, len(sys.argv)): # i is starting from 1 because 0th position has program name that needs to ignored
    input_list.append(int(sys.argv[i]))

print(f"Orignal List: {input_list}")
print(f"Sorted List with regular bubble sort: {bs.bubble_sort(input_list)}")
print(f"Sorted List with optimized bubble sort: {bs_opt.bubble_sort(input_list)}")

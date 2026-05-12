import partition as p

def quick_sort(numbers, low, high):
    if low < high :
        pivot_index = p.partition_array_reccursive(numbers, low, high)
        # print(numbers) # Uncomment to see step wise changes to list data
        quick_sort(numbers, low, pivot_index - 1)
        quick_sort(numbers, pivot_index + 1, high)
    return numbers

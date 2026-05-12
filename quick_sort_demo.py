import sys
import quick_sort as qs

input_num = [int(value) for value in sys.argv[1:]]

print("Input Numbers: ", input_num)
print(f"Sorted List: {qs.quick_sort(input_num, 0, len(input_num) - 1)}")
import insertion_sort as ins
import sys
input_numbers = []

for i in range(1, len(sys.argv)):
    input_numbers.append(int(sys.argv[i]))

print(f"Orignal List: {input_numbers}")
print(f"Sorted List: {ins.insertion_sort(input_numbers)}")
import selection_sort as sel
import sys

num_list = []

for i in range(1, len(sys.argv)):
    num_list.append(sys.argv[i])

print(f"Orignal List: {num_list}")
print(f"Sorted List: {sel.selection_sort(num_list)}")
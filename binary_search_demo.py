import sys

import binary_search

input_numbers = []
print(f'User given elements are: ')
for i in range(1, len(sys.argv)): ## i is starting from 1 because 0th position has program name that needs to ignored
    input_numbers.append(int(sys.argv[i]))

print(f'User given elements are: {input_numbers}')

search_element = float(input("Enter the element to be searched: "))
search_index = binary_search.binary_search(search_element, input_numbers)

if search_index == -1:
    print(f"The search element {search_element} is not found.")
else:
    print(f"The search element {search_element} is found at search index {search_index + 1}.")

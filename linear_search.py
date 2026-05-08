def sequential_search(search_element, elements):
    for i in range(len(elements)):
        if elements[i] == search_element:
            return i
    return -1

input_size = int(input("Enter the size of list: "))

elements = []

print(f"Enter the {input_size} elements of the list: ")

for i in range(input_size):
    element = float(input())
    elements.append(element)

print("User given elements are \n", elements)

search_element = float(input("Enter the element to be searched: "))
search_index = sequential_search(search_element, elements)

if search_index == -1:
    print(f"The search element {search_element} is not found.")
else:
        print(f"The search element {search_element} is found at search index {search_index + 1}.")

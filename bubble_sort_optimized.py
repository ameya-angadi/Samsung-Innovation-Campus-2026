def bubble_sort(list_of_elements):
    for i in range(0, len(list_of_elements) - 2):
        sorted = True
        for j in range(0, len(list_of_elements) - 2 - i):
            if list_of_elements[j] > list_of_elements[j + 1]:
                list_of_elements[j], list_of_elements[j + 1] = list_of_elements[j + 1], list_of_elements[j]
                sorted = False
        if sorted:
            break
    return list_of_elements
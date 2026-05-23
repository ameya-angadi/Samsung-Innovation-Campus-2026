import numeros_problem_functions as f

list1 = []
list2 = []

list_miss_no = []

f.input_list(list1)
f.input_list(list2)

f.find_missing_num(list1, list2, list_miss_no)
list_miss_no.sort()
print(list_miss_no)
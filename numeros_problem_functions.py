def input_list(list_num = []):
    m = int(input("Enter number of elements is list:"))
    print("Enter List\'s elements: ")
    for i in range(0, m):
        list_num.append(int(input()))

def find_missing_num(list1, list2, list_miss_no):
    for num1 in list1:
        is_num_present = 1
        for num2 in list2:
            count1 = list1.count(num1)
            count2 = list2.count(num2)
            if count1 == count2 and num1 == num2:
                is_num_present = 1
                break
            else:
                is_num_present = 0
        if is_num_present == 0:
            if num1 not in list_miss_no:
                list_miss_no.append(num1)



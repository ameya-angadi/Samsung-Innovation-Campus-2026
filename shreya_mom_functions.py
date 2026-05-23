def input_list(list_num, text = ""):
    n = int(input(f"Enter number of elements in list({text} Shoes):"))
    if n > 1:
        print(f"Enter List\'s elements ({text} Shoes): ")
        for i in range(0, m):
            list_num.append(int(input()))
    else:
        print("n < 1, hence shoes are not available to purchase")

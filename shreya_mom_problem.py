import shreya_mom_functions as f

list_ava_shoes = []
list_pur_shoes = []

f.input_list(list_ava_shoes, "Available")
list_ava_shoes.sort()
print("Available shoes with their cost:", list_ava_shoes)

p = int(input("Enter number of shoes to be purchased: "))

for i in range(p):
    list_pur_shoes.append(list_ava_shoes[i])

if sum(list_pur_shoes) < 0:
    print("Total Money they will earn: ", -sum(list_pur_shoes))
    
else:
    print("Total Money they will earn: 0")

people = [(7, 'Shreyam', 1, 19, 'Mysore'), 
(8, 'Ameya', 0, 19, 'Bengaluru'), 
(9, 'Kabir', 1, 99, 'Delhi'), 
(10, 'Kaushal', 1, 3, 'Haryana')]
print('-' * 40)
print('%-2s %-15s %-7s %-3s %s'%('ID', 'NAME', 'GENDER', 'AGE', 'LOCATION'))
print('-' * 40)
gender = ''
for person in people:
    if person[2] == 0:
        gender = 'Male'
    else:
        gender = 'Female'
    print('%-2d %-15s %-7s %-3d %s'%(person[0], person[1], gender, person[3], person[4]))
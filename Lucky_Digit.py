#input_number = 12345
#lucky_digit = 6

#input_number = 789
#lucky_digit = 6

#input_number = 257
#lucky_digit = 5

inputNum = int(input("Enter a number to get your lucky number: "))
sumOfDigits = 0

while inputNum != 0:
    sumOfDigits += (inputNum%10)
    inputNum = inputNum//10
    if sumOfDigits > 9 and inputNum == 0:
        inputNum, sumOfDigits = sumOfDigits, 0

print("Lucky Digit: ", sumOfDigits)
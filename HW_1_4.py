number = int(input('Enter a positive integer number:'))
curr_digit = 0
while number != 0:
    if curr_digit < number % 10:
        curr_digit = number % 10
    if curr_digit == 9:
        break
    number = number//10
print('\nThe biggest digit in your number is ', curr_digit)


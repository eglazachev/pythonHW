# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num_1, num_2):
    try:
        answer = num_1 / num_2
        return print(f'Division result is {answer}')
    except ZeroDivisionError:
        print('Can\'t divide by zero')


division(float(input('Enter first number ')), float(input('Enter second number ')))

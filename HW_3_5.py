# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_sum():
    result = 0
    nums = input('Enter single or a list of numbers, split them with space: ').split()
    print(nums)
    leave = 'n'
    while True:
        for num in nums:
            try:
                result += float(num)
            except ValueError:
                leave = 'y'
                break
        if leave == 'y':
            break
        nums = input(f'Current sum = {result},\n'
                     f'Type q to leave or\n'
                     f'Enter a number or a list of numbers, split them with space: ').split()
    print('\nTotal sum = ', result)


my_sum()

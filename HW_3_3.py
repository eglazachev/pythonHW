# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def among_us(*args):
    nums = [*args]
    a = max(*args)
    nums.remove(a)
    result = a + max(nums)
    print(result)


among_us(-11, -2, -3, -7.8, -1)

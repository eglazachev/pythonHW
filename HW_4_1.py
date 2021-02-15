# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


import sys

work_time, money_per_hour, bonus = map(float, sys.argv[1:])
print('Your salary for {} hours is {}'.format(work_time, work_time * money_per_hour + bonus))

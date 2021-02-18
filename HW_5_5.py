# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("task5.txt", 'w') as file:
    for i in range(1, 20):
        file.write(str(randint(1, 100))+' ')
with open("task5.txt", 'r') as file:
    num_sum = 0
    for el in file.read().split():
        num_sum += int(el)
print(num_sum)

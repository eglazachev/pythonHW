# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

old_list = [4, 5, 6, 23, 4, 6, 22, 234, 54, 3, 2, 2, 4, 345, 4]
print([old_list[i] for i in range(1, len(old_list) - 1) if old_list[i] > old_list[i-1]])


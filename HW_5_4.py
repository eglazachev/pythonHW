# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numerals = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open("task4_ru.txt", 'x', encoding='utf-8') as file_ru:
    with open("task4_en.txt", 'r') as file_en:
        for line in file_en:
            print(numerals.get(int(line.split()[2]))+' '+line.split()[1]+' '+line.split()[2]+'\n', file=file_ru)
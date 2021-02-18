# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("task2.txt", 'r') as file:
    content = file.readlines()
    print(len(content))
    for el in content:
        print(len(el.split()))

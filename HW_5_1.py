# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task1.txt", 'x') as file:
    while True:
        user_text = input('Type smth here')
        if user_text == '':
            break
        else:
            file.write(user_text + '\n')

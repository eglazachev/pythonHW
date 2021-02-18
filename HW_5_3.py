# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

avg_salary = 0
with open("task3.txt", 'r') as file:
    content = file.readlines()
    for employes in content:
        if int(employes.split()[1]) > 20000:
            print(employes.split()[0])
        avg_salary += int(employes.split()[1])
    print('Average salary is', avg_salary/len(content))
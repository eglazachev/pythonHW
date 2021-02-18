# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json


firm_stats = {}
avg_earn = 0
with open("task7.txt", 'r', encoding='utf-8') as file:
    companies = file.readlines()
    print(companies)
    for line in companies:
        earn = int(line.split()[2]) - int(line.split()[3])
        print(line, 'Earnings: ', earn, '\n')
        firm_stats.update({line.split()[0]: earn})
        if earn >= 0:
            avg_earn += earn
    print('Average earnings: ', avg_earn/len(companies))
stats = [firm_stats, {"average_profit": avg_earn/len(companies)}]
with open("task7.json", 'w') as json_file:
    json.dump(stats, json_file)

# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_info(form):
    user_list = dict.fromkeys(form)
    for item in user_list:
        user_list[item] = input(f'Type your {item} here please ')
    print(user_list)


questionnaire = ['first name', 'last name', 'year of birth', 'city', 'e-mail', 'phone']
user_info(questionnaire)


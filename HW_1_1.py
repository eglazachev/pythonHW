user_name = input('Как Вас зовут?\nВведите Имя:')
user_age = int(input('Сколько Вам лет?\nВведите возраст:'))
user_city = input('Где Вы родились?\nВведите название города:')
user_power_lift = float(input('Скок жмёшь лёжа? А?\nВведите массу в килограммах:'))

print('\nПользователю с именем {0} {1} лет, родившись в городе {2} {0} жмёт {3} кг от груди!'
      .format(user_name, user_age, user_city, user_power_lift))

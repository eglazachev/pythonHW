# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)


class Worker:
    income = {'wage': 25000, 'bonus': 8500}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.income


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = self.income.get('wage') + self.income.get('bonus')
        return total_income


stuff_member = Position('Andrew', 'Olofsson', 'accountant')
print(stuff_member.get_full_name())
print(stuff_member.get_total_income())
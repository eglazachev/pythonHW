# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'{self.name} is on its way')

    def stop(self):
        return print(f'{self.name} is stopped now')

    def turn(self, way):
        return print(f'{self.name} is turning to the {way}')

    def show_speed(self):
        return print(f'{self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'{self.name} is exceeding the speed limit')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'{self.name} is exceeding the speed limit')


my_car = TownCar(299792458, 'blue', 'Malcolm', False)
my_car.go()
my_car.stop()
my_car.turn('stars')
my_car.show_speed()

print(my_car.name)
print(my_car.speed)
print(my_car.color)

his_car = WorkCar(40, 'black', 'Buddy', False)
print(his_car.name)
his_car.show_speed()
his_car.turn('dump station')

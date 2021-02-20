# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return print('Let\'s begin the draw')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Pen')

    def draw(self):
        return print(f'Let\'s begin the draw with {self.title}')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Pencil')

    def draw(self):
        return print(f'Let\'s begin the draw with {self.title}')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Handle')

    def draw(self):
        return print(f'Let\'s begin the draw with {self.title}')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()

class Horse:
    """Класс, описывающий лошадь"""
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance    # пройденный путь
        self.sound = sound              # звук, который издаёт лошадь
        super().__init__()  # при создании объекта обращаемся также к конструктору класса Eagle, по цепочке наследования

    def run(self, dx):
        self.x_distance = self.x_distance + dx    # изменение дистанции
        return self.x_distance


class Eagle:
    """Класс, описывающий орла"""
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance    # высота полёта
        self.sound = sound  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance = self.y_distance + dy    # изменение высоты
        return self.y_distance


class Pegasus(Horse, Eagle):
    """Класс, описывающий пегаса"""
    def move(self, dx, dy):
        self.run(dx)   # изменение дистанции
        self.fly(dy)   # изменение высоты

    def get_pos(self):
        return (self.x_distance, self.y_distance)   # текущее положение пегаса

    def voice(self):
        print(self.sound)    # значение унаследованного атрибута sound ОРЛА


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# print(dir(p1))    # посмотреть атрибуты объекта
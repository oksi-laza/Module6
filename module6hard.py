from math import pi, sqrt


class Figure:  # Фигура
    """
    :param __sides (int) - список сторон
    :param __color (int, int, int) - список цветов в формате RGB
    :param filled (bool) - закрашенный
    """
    sides_count = 0  # количество сторон

    def __init__(self, color, *sides, filled=True):
        entered_color = []  # сообщение о том, что при указании параметра color введены недопустимые значения
        for i in color:
            if 0 <= i <= 255:
                i = True
                entered_color.append(i)
            else:
                i = False
                entered_color.append(i)
        if all(entered_color):
            self.__color = list(color)
        else:
            print(f'В объекте {self}\n'
                  'Вы неправильно указали значения атрибута color.\n'
                  'Измените введенные значения в интервале от 0 до 255.\n'
                  'Иначе дальнейшая работа с объектом будет возможна не в полном объеме.')
        # self.__color = list(color)    # прежняя версия, если без проверки цвета при передаче атрибутов
        self.filled = filled
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = []
            while len(self.__sides) < self.sides_count:
                self.__sides.append(1)

    def get_color(self):
        """ Возвращает список RGB цветов """
        return self.__color

    def __is_valid_color(self, r, g, b):
        """
        Служебный метод, принимает параметры r, g, b,
        который проверяет корректность переданных значений перед установкой нового цвета.
        """
        self.color_new = list((r, g, b))
        self.colors_check = []
        for i in self.color_new:
            if 0 <= i <= 255:
                i = True
                self.colors_check.append(i)
            else:
                i = False
                self.colors_check.append(i)
        return self.colors_check

    def set_color(self, r, g, b):
        """
        Изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность.
        Если введены некорректные данные, то цвет остаётся прежним.
        """
        self.__is_valid_color(r, g, b)
        if all(self.colors_check):
            self.__color = self.color_new
            return self.__color
        else:
            return self.__color

    def get_sides(self):
        """ Возвращает значение атрибута __sides """
        return self.__sides

    def __is_valid_sides(self, *sides):
        """
        Служебный метод, принимает неограниченное кол-во сторон,
        возвращает True, если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        возвращает False - во всех остальных случаях.
        """
        if len(sides) != len(self.__sides):  # если len(кортеж введенных сторон) != len(список имеющихся сторон):
            return False
        else:
            check_sides = []
            for i in sides:
                if isinstance(i, int):
                    check_sides.append(True)
                else:
                    check_sides.append(False)
            if all(check_sides):  # если в списке 'check_sides' все True, то возвращаем True
                return True
            else:
                return False

    def set_sides(self, *sides):
        """
        Изменяет атрибут '__sides' на новые значения,
        предварительно проверив их на корректность в методе '__is_valid_sides'.
        Если введены некорректные данные, то стороны остаются прежних размеров.
        """
        if self.__is_valid_sides(*sides) is True:
            self.__sides = list(sides)
            return self.__sides
        else:
            return self.__sides

    def __len__(self):
        """ Возвращает периметр фигуры"""
        perimeter = sum(self.__sides)
        return perimeter


class Circle(Figure):  # Круг
    """
    У круга 1 сторона(длина), значит в параметрах необходимо передать только одно значение длины,
    иначе сторона будет равна 1.
    """
    sides_count = 1  # количество сторон

    def __init__(self, color, *sides, filled=True):  # все атрибуты класса Figure
        super().__init__(color, *sides, filled=filled)
        self.__radius = self.__radius_calculation()  # при создании объекта радиус рассчитывается от заданной стороны
        # print(f'Радиус этого круга равен: {self.__radius}')  # если нужно увидеть сразу, какой радиус у созданного круга

    def __radius_calculation(self):    # метод расчета радиуса
        len_circle = self.get_sides()[0]
        self.__radius = len_circle / (2 * pi)
        return round(self.__radius, 4)

    def get_square(self):
        """
        Возвращает площадь круга (расчет через радиус).
        Получаем радиус через метод get_radius, так как в нем происходит расчёт радиуса заново,
        в зависимости от текущей длины круга.
        """
        square_circle = pi * (self.get_radius() ** 2)
        return round(square_circle, 4)

    def get_radius(self):
        """ Возвращает радиус круга. Расчёт радиуса от текущей длины круга (важно, если было изменение сторон) """
        self.__radius = self.__radius_calculation()
        return self.__radius


class Triangle(Figure):  # Треугольник
    """
    У треугольника 3 стороны, значит в параметрах необходимо передать три значения длины.
    Если переданных значений длины будет больше или меньше, то все стороны треугольника будут равны 1.
    Важно знать правило, какой длины должны быть стороны, чтобы возможно было построить треугольник:
    сумма двух сторон треугольника всегда больше третьей стороны (a<b+c; b<a+c; c<a+b)
    """
    sides_count = 3  # количество сторон

    def __init__(self, color, *sides, filled=True):  # все атрибуты класса Figure
        super().__init__(color, *sides, filled=filled)
        self.__height = self.__height_calculation()    # высота треугольника
        # print(f'Высота этого треугольника равна: {self.__height}')    # если хотим сразу выводить высоту треугольника

    def __height_calculation(self):
        h_sides_0 = (2 * self.get_square()) / self.get_sides()[0]    # высота, где основанием является '__sides[0]'
        h_sides_1 = (2 * self.get_square()) / self.get_sides()[1]    # высота, где основанием является '__sides[1]'
        h_sides_2 = (2 * self.get_square()) / self.get_sides()[2]    # высота, где основанием является '__sides[2]'
        self.__height = [round(h_sides_0, 4), round(h_sides_1, 4), round(h_sides_2, 4)]
        return self.__height

    def get_square(self):
        """ Возвращает площадь треугольника """
        half_perimeter = self.__len__() / 2
        square_triangle = sqrt(half_perimeter *
                               (half_perimeter - self.get_sides()[0]) *
                               (half_perimeter - self.get_sides()[1]) *
                               (half_perimeter - self.get_sides()[2]))
        return round(square_triangle, 4)

    def get_height(self):
        self.__height = self.__height_calculation()
        return self.__height


class Cube(Figure):  # Куб
    """
    У куба 12 сторон, но в параметр необходимо передать только одно значение длины,
    иначе сторона будет равна 1.
    """
    sides_count = 12  # количество сторон

    def __init__(self, color, *sides, filled=True):  # все атрибуты класса Figure
        if len(sides) != 1 or len(sides) == self.sides_count:
            super().__init__(color, 1, filled=filled)
        else:
            sides = (sides) * self.sides_count
            super().__init__(color, *sides, filled=filled)

    def __is_valid_sides(self, *sides):  # переопределим метод '__is_valid_sides' для класса Cube
        """
        Служебный метод, принимает неограниченное кол-во сторон,
        возвращает True, если указано одно значение для размера стороны и это значение - целое положительное число,
        возвращает False - во всех остальных случаях.
        """
        if len(sides) == 1 and isinstance(*sides, int):  # перед проверкой числа, нужно его извлечь из кортежа
            return True
        else:
            return False

    def set_sides(self, *sides):  # переопределим метод 'set_sides' для класса Cube
        """
        Изменяет атрибут '__sides' на новые значения,
        предварительно проверив их на корректность в методе '__is_valid_sides'.
        Если введены некорректные данные, то стороны остаются прежних размеров.
        """
        if self.__is_valid_sides(*sides) is True:
            new_sides_cube = (sides) * self.sides_count
            super().set_sides(*new_sides_cube)

    def get_volume(self):
        """ Возвращает объём куба """
        len_side = self.get_sides()[0]
        volume_cube = len_side ** 3
        return volume_cube


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # цвет изменится
cube1.set_color(300, 70, 15)  # цвет останется прежний
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



# Дополнительные проверки
print('----------------------------------------------------')
triangle1 = Triangle((201, 32, 184), 4, 7, 6) # сумма двух сторон треугольника всегда больше третьей стороны
triangle2 = Triangle((5, 112, 49), 9, 18)     # создала новые объекты для проверки
circle2 = Circle((50, 50, 40), 28, 18)
cube2 = Cube((52, 208, 139), 15)    # для проверки переданных сторон

# Проверка на количество переданных сторон:
print(f'Размер и количество сторон треугольника_1: {triangle1.get_sides()}')
print(f'Размер и количество сторон треугольника_2: {triangle2.get_sides()}')
print(f'Размер и количество сторон круга_2: {circle2.get_sides()}')
print(f'Размер и количество сторон куба_2: {cube2.get_sides()}')

# Проверка рассчета периметра у разных фигур
print(f'Периметр треугольника_1: {triangle1.__len__()}')
print(f'Периметр треугольника_2: {triangle2.__len__()}')
print(f'Периметр круга_2: {circle2.__len__()}')
print(f'Периметр куба_2: {cube2.__len__()}')

# Проверка методов класса Circle
print('-------------------------------\n'
      'Проверка методов класса Circle')
print(f'Площадь круга_1: {circle1.get_square()}')
print(f'Радиус круга_1: {circle1.get_radius()}')
print(f'Размер и количество сторон этого круга_1: {circle1.get_sides()}')

# Проверка методов класса Cube и изменение сторон
print('----------------------------\n'
      'Проверка методов класса Cube')
cube3 = Cube((52, 208, 139), 17)
print(cube3.get_sides())
print(f'Объем куба_3: {cube3.get_volume()}')
cube3.set_sides(12, 25)  # стороны куба НЕ изменятся
print(cube3.get_sides())
cube3.set_sides(12)  # стороны куба Изменятся
print(cube3.get_sides())

# Проверка методов класса Triangle
print('--------------------------------\n'
      'Проверка методов класса Triangle')
print(f'Площадь треугольника_1: {triangle1.get_square()}')
print(f'Высота треугольника_1: {triangle1.get_height()}')
print(f'Размер и количество сторон этого треугольника_1: {triangle1.get_sides()}')
print(f'Площадь треугольника_2: {triangle2.get_square()}')
print(f'Высота треугольника_2: {triangle2.get_height()}')
print(f'Размер и количество сторон этого треугольника_2: {triangle2.get_sides()}')

# Проверка на изменение сторон у треугольника, а также изменение цвета
print('--------------------------------------------------------------------\n'
      'Проверка на изменение сторон у треугольника, а также изменение цвета')
triangle1.set_sides(15)  # стороны треугольника НЕ изменятся
triangle2.set_sides(12, 7, 18)  # стороны треугольника Изменятся
print(f'Новые размеры треугольника_1: {triangle1.get_sides()}')
print(f'Новые размеры треугольника_2: {triangle2.get_sides()}')
print(f'Высота треугольника_2 после изменения сторон: {triangle2.get_height()}')
print(f'Площадь треугольника_2 после изменения сторон: {triangle2.get_square()}')

triangle1.set_color(189, 98, 206)  # цвет изменится
triangle2.set_color(550, 74, 83)   # цвет останется прежний
print(f'Цвет треугольника_1: {triangle1.get_color()}')
print(f'Цвет треугольника_2: {triangle2.get_color()}')

# Проверка на правильный ввод атрибута color с самого начала - вывод сообщения
print('---------------------------------------------------------------\n'
      'Проверка на правильный ввод атрибута color при создании объекта')
circle3 = Circle((100, 50, 256), 32)

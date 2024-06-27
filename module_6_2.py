class Vehicle:
    """
    Класс транспорта, в котором нельзя просто так поменять цвет, мощность двигателя и прочие свойства
    """
    __COLOR_VARIANTS = ['blue', 'red', 'black', 'white', 'silver', 'brown']

    def __init__(self, owner, __model, __color, __engine_power):
        """
        :param owner: (str) - владелец транспорта, владелец может меняться
        :param __model: (str) - модель (марка) транспорта, мы не можем менять название модели
        :param __color: (str) - название цвета, мы не можем менять цвет автомобиля своими руками
        :param __engine_power: (int) - мощность двигателя, мы не можем менять мощность двигателя самостоятельно.
        """
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5    # в седан может поместиться только 5 пассажиров



# Код для проверки
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

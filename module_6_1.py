class Animal:
    alive = True            # живой
    fed = False             # накормленный

    def __init__(self, name):
        self.name = name    # индивидуальное название каждого животного

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Plant:
    edible = False          # съедобность

    def __init__(self, name):
        self.name = name     # индивидуальное название каждого растения


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive, f'     Объект {a1.name} является живым?')   # расшифровка значения для себя
print(a2.fed, f'    Объект {a2.name} является сытым?')      # расшифровка значения для себя
a1.eat(p1)
a2.eat(p2)
print(a1.alive, f'    Объект {a1.name} после кормления является живым?')   # расшифровка значения для себя
print(a2.fed, f'     Объект {a2.name} после кормления является сытым?')   # расшифровка значения для себя

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

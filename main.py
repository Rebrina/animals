# реализовать классы животных
class Animal:
    def __init__(self, name: str, weight: float, height: float):
        self.name = name
        self.weight = weight  # кг
        self.height = height  # cм

    def voice_type(self):
        print(self.name, self.voice_type)

    def hunger(self):
        print(self.name, 'eated')


class Bird(Animal):
    def wings_amplitude(self, wings):
        print(self.name, 'размах крыльев', wings)

    def eggs(self, egg):
        print(self.name, 'яйца =', egg)


class Mammal(Animal):
    def tails_lenght(self, tails):
        print(self.name, 'длина хвоста', tails)

    def milk(self, milk):
        print(self.name, 'молоко =', milk)


class Gans(Bird):
    # откормить
    def eat(self, max_weight):
        print(self.name, 'вес набран')


class Cow(Mammal):
    # выпас
    def walk(self, walk):
        print(self.name, 'выпасено')


class Sheep(Mammal):
    # стричь
    def wool(self, wool):
        print(self.name, 'шерсть =', wool)


class Chiken(Bird):
    # откормить
    def eat(self, max_weight):
        print(self.name, 'вес набран')


class Goat(Mammal):
    # выпас
    def walk(self, walk):
        print(self.name, 'выпасено')


class Duck(Bird):
    def fur_hair(self, fur_hair):
        print(self.name, 'пух собран')


gans_1 = Gans('Серый', 2, 30)
gans_2 = Gans('Белый', 2.5, 30)
cow_1 = Animal('Манька', 20, 100)
sheep_1 = Animal('Барашек', 15, 90)
sheep_2 = Animal('Кудрявый', 16, 90)
chiken_1 = Bird('Ко-Ко', 3, 20)
chiken_2 = Bird('Кукареку', 3.5, 22)
goat_1 = Animal('Рога', 14, 35)
goat_2 = Animal('Копыта', 14.5, 36)
duck_1 = Bird('Кряква', 5, 17)

all_animals = [gans_1, gans_2, cow_1, sheep_1, sheep_2, chiken_1, chiken_2, goat_1, goat_2, duck_1]

# кормить всех
for animal in all_animals:
    animal.hunger()

# общий вес
weight_all_animals = 0
for animal in all_animals:
    weight_all_animals = weight_all_animals + animal.weight
print('Total weight', weight_all_animals)

# вывести, у кого вес больше
max_weight = ''
for animal in all_animals:
    if max_weight is '':
        max_weight = animal
    elif animal.weight > max_weight.weight:
        max_weight = animal
print('Самое тяжелое животное', max_weight.name)
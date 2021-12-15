class Animals:
    def __init__(self, name, age, food, sleep_hours):
        self.name = name
        self.age = age
        self.food = food
        self.sleep_hours = sleep_hours
    
    def info(self):
        print(f'Меня зовут {self.name}. Мне {self.age}.')
        print(f'Моя еда: {self.food}.')
        print(f'Я сплю по {self.sleep_hours} часов в день.')

class Mammals(Animals):
    def __init__(self, name, age, food, sleep_hours, is_fluffy):
        super().__init__(name, age, food, sleep_hours)
        self.is_fluffy = is_fluffy

    def info(self):
        print(f'Я млекопитающий зверёк. Меня зовут {self.name}. Мне {self.age} лет')
        print(f'Моя еда: {self.food}.')
        print(f'Я сплю по {self.sleep_hours} часов в день.')
        if self.is_fluffy:
            print(f'Я белый и пушистый :)')

class Cat(Mammals):
    def __init__(self, name, age, sleep_hours, count_past_lives, is_short_paws):
        super().__init__(name, age, ['рыбка', 'молочко', 'Whiskas'], sleep_hours, is_fluffy=True)
        self.count_past_lives = count_past_lives
        self.is_short_paws = is_short_paws
        self.is_sweetie_pie = True

    def info(self):
        print(f'Я котик {self.name}. Я сладкая булочка. Мне {self.age} лет')
        print(f'Моя еда: {self.food}.')
        print(f'Я сплю по {self.sleep_hours} часов в день.')
        print(f'Это моя {self.count_past_lives}-я жизнь.')
        if self.is_short_paws:
            print(f'Мои лапки очень короткие, я за тобой не успею.')

    def make_sound(self):
        print(f'{self.name}: *мяу*')
        
class Dog(Mammals):
    def __init__(self, name, age, food, sleep_hours, is_angry):
        super().__init__(name, age, food, sleep_hours, is_fluffy=True)
        self.is_angry = is_angry

    def info(self):
        if self.is_angry:
            print(f'Я злая собака. Не трогай меня. Меня зовут {self.name}. Мне {self.age} лет')
        else:
            print(f'Я милый пёсик.Меня зовут {self.name}.Мне {self.age} лет')
        print(f'Моя еда: {self.food}.')
        print(f'Я сплю по {self.sleep_hours} часов в день.')

    def make_sound(self):
        print(f'{self.name}: гав')
    
    def bite(self, human):
        print(f'{self.name} делает кусь')

    def lick_face(self, human):
        print(f'{self.name} облизывает лицо {human.name}')

class Human(Mammals):
    def __init__(self, name, age, food, sleep_hours, gender, character, is_happy):
        super().__init__(name, age, food, sleep_hours, is_fluffy=False)
        self.gender = gender
        self.character = character
        self.is_happy = is_happy
    
    def info(self):
        if self.gender == 'ж':
            print(f'Я {self.character} женщина.')
        else:
            print(f'Я {self.character} мужчина.')
        print(f'Меня зовут {self.name}. Мне {self.age} лет')
        print(f'Моя еда: {self.food}.')
        print(f'Я сплю по {self.sleep_hours} часов в день.')
        if self.sleep_hours > 10:
            self.is_happy = True
        if self.name == 'Olya' or self.name == 'Pasha':
            self.is_happy = False
        if not self.is_happy:
            print(f'I am dead inside but still horny')

    def pet_the_cat(self, cat):
        print(f'{self.name} гладит {cat.name}.')
        cat.make_sound()
        self.is_happy = True

    def pet_the_dog(self, dog):
        if dog.is_angry:
            print(f'{self.name} хочет погладить {dog.name}.')
            dog.bite(Human)
            dog.make_sound()
            self.is_happy = False
        else:
            print("{self.name} гладит {dog.name}")

class Student(Human):
    def __init__(self, name, age, food, sleep_hours, gender, character, course, count_homework):
        super().__init__(name, age, food, sleep_hours, gender, character, is_happy = False)
        self.course = course
        self.count_homework = count_homework

    def info(self):
        print(f'Я {self.character} студент {self.course} курса. Меня зовут {self.name}. Мне {self.age} лет')
        print(f'Моя еда: {self.food}.')
        print(f'Я сплю по {self.sleep_hours} часов в день.')
        print(f'I am dead inside but still horny')

Pasha1 = Cat('Pasha', 20, 6, 9, False)
Olya1 = Human('Olya', 10, 'тортики', 12, 'ж', 'сильная и независимая', False)
Pasha1.info()
print()
Olya1.info()
print()
Olya1.pet_the_cat(Pasha1)

print()

Pasha2 = Human('Pasha', 20, 'всё', 6, 'м', 'сладкая булочка', False)
Olya2 = Dog('Olya', 10, 'люди', 0, True)
Pasha2.info()
print()
Olya2.info()
print()
Pasha2.pet_the_dog(Olya2)

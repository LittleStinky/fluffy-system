import random

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

    def session(self):
        self.sleep_hours = 0
        mood = random.randint(1, 4)
        if mood == 1:
            print(f'Пожалуйста, не валите нас, мы же котятки.')
        elif mood == 2:
            print(f'Ничего не спрашивайте, я сегодня не в настроении быть смешнявкой.')
        elif mood == 3:
            if self.gender == 'м':
                print(f'О нет, моя нервная система, которую я выстраивал полгода.')
            else:
                print(f'О нет, моя нервная система, которую я выстраивала полгода.')
        elif mood == 4:
            print(f'Работаю по графику сутки через силу.')   

Somebody = Student('Somebody', 19, 'кофе', 0, 'ж', 'никакой', 2, 10000)
Somebody.session();

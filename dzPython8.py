class Animals:
    def __init__(self, gender, age, weight):
        self.gender = gender
        self.ages = age
        self.weight = weight

    def __eq__(self, __o: object) -> bool:
        pass

class Mammals(Animals):
    def __init__(self, gender, age, weight, name, amount_of_children):
        super().__init__(gender, age, weight)
        self.amount_of_children = amount_of_children
        self.name = name

class Human(Mammals):
    def __init__(self, gender, age, weight, name, amount_of_children, height):
        super().__init__(gender, age, weight, name, amount_of_children)
        self.height = height
        self.name = name

    def work(self, string):
        print(f'{self.name} working here: {string}')
    

class Cat(Mammals):
    def __init__(self, gender, age, weight, name, amount_of_children, door):
        super().__init__(gender, age, weight, name, amount_of_children)
        self.door = door

    def Open(self):
        if self.door == "opened" or "открыто":
            print(f'{self.name} says: wft?!')
        else:
            print(f'{self.name} says: please open the door')


class Dog(Mammals):
    def __init__(self, gender, age, weight, name, amount_of_children, trigger):
        super().__init__(gender, age, weight, name, amount_of_children)
        self.trigger = trigger
        
    def triggers(self):
        if self.trigger == "Кот":
            print(f'the dog, {self.name}, is running')
        else:
            print(f'nothing to do for {self.name}')

class Student(Human):
    def __init__(self, gender, age, weight, name, amount_of_children, height, dz_count, college):
        super().__init__(gender, age, weight, name, amount_of_children, height)
        self.dz_count = dz_count
        self.college = college
    
    def __lt__(self, other):
        return self.dz_count < other.dz_count
    
    def __eq__(self, other):
        return self.dz_count == other.dz_count

    def __le__(self, other):
        return self.dz_count <= other.dz_count    

Markisa = Cat("male", 2, 6, "Boris", 0, "открыто")
print(Markisa.gender, Markisa.ages, Markisa.weight, Markisa.amount_of_children, Markisa.door)
Markisa.Open()

Mike = Student("male", 15, 50,"Mike", 0, 160, 5, "Dem")
Sam = Student("male", 15, 50,"Sam", 0, 160, 10, "qwe")
print(Mike > Sam)
print(Mike == Sam)
print(Mike <= Sam)

class Person(object):
    def __init__(self, age):
        self.age = age

    def drive(self):
        if self.age <= 17:
            raise Exception('年齢が達していないです!!!')
        print('You can drive now')


class Baby(Person):
    def __init__(self, age):
        if age > 4:
            raise ValueError
        super().__init__(age)


class Adult(Person):
    def __init__(self, age):
        if age < 17:
            raise ValueError
        super().__init__(age)


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def ride(self, person):
        person.drive()


adult = Adult(23)
print(adult.age)
baby = Baby(2)
print(baby.age)
car = Car()
car.ride(adult)
car.ride(baby)

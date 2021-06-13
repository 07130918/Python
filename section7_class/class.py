class Person(object):
    # selfを忘れないように!
    def __init__(self, name):
        self.name = name
        print(f'init: {self.name}')

    def say_something(self):
        print(f"Hello I'm {self.name}")
        self.run(3)

    def run(self, num):
        print('run' * num)


person = Person('kota')
person.say_something()

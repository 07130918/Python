import inspect


class Person(object):
    # selfを忘れないように!
    # ↓constructor
    def __init__(self, name):
        self.name = name
        print(f'init: {self.name}')

    def say_something(self):
        print(f"Hello I'm {self.name}")
        self.run(3)

    def run(self, num):
        print('run' * num)

    # ↓destructor
    def __del__(self):
        print('Good bye')


person = Person('kota')
person.say_something()

del person
print('------------')

print([x for x in inspect.getmembers(Person)])

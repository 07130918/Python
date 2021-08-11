class Something(object):

    def __init__(self, name) -> None:
        self.name = name
        print(f'init: {self.name}')

    def greeting(self):
        print(f'Hello I\'m {self.name}')
        self.run(3)

    def run(self, times):
        print('run' * times)

    def __del__(self):
        print('Good bye')


print(Something)
kota = Something('kota')
kota.greeting()
print(kota)


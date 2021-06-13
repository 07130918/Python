class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    pass


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False, pass_word='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.pass_word = pass_word

    # getter
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # setter
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.pass_word == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print('-------------------------')

toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('-------------------------')

tesla_car = TeslaCar(pass_word='456')
print(tesla_car.model)
# setter, getter関数は()なしで呼び出せる(is_enableにTrueが入る)
tesla_car.enable_auto_run = True
print(f'Auto run mode: {tesla_car.enable_auto_run}')
tesla_car.run()
tesla_car.auto_run()

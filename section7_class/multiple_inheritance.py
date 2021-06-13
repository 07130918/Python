class Person(object):
    def talk(self):
        print('let us talk')

    def run(self):
        print('person running')


class Car(object):
    def run(self):
        print('buuun')

    def stop(self):
        print('brake')


class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

    def all(self):
        self.talk()
        self.run()
        self.stop()
        self.fly()


person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.stop()
person_car_robot.fly()
print('-----------------')
person_car_robot.all()

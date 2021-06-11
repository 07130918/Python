# import l_package.tools.utils
# from l_package.tools import utils as u

# from l_package.talk import *
from l_package.talk import animal, human
from l_package.tools import utils

result = utils.say_twice("hello")
print(result)

print(human.sing())
print(human.cry())

print(animal.sing())
print(animal.cry())

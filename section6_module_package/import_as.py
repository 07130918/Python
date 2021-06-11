# import l_package.utils
# from l_package import utils as u
from l_package.tools import utils

from l_package.talk import human

result = utils.say_twice("hello")
print(result)

print(human.sing())
print(human.cry())

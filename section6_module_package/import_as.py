# import python_package.utils
# from python_package import utils as u
from python_package import utils
from python_package.python_package_deeper import human

result = utils.say_twice('hello')
print(result)

print(human.sing())
print(human.cry())

import pprint

fruits = ['apple', 'orange', 'banana', 'peach', 'mango']
fruits.insert(0, fruits[:])

pp = pprint.PrettyPrinter()
pp.pprint(fruits)

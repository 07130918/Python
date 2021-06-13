class Person(object):
    # class var
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()
print(id(a.kind), id(a.kind) == id(b.kind))


# 望ましくない例
class T(object):

    words = []

    def add_words(self, word):
        self.words.append(word)


c = T()
c.add_words('add 1')
c.add_words('add 2')
d = T()
d.add_words('add 1')
d.add_words('add 2')
print(c.words)
print(d.words)

class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(name):
        print(f'about human {name}')


a = Person()
print('a: ', a)
b = Person
print('b: ', b)

# インスタンス化していなくてもクラス変数,クラスメソッドにはアクセス可能
print(b.kind)
print(b.what_is_your_kind())

# 直接呼び出し
print(Person.kind)
print(Person.what_is_your_kind())

Person.about('kota')

class Word(object):

    # __があるのが特殊メソッド
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word('TEST')
w2 = Word('test')
# __str__
print(w)
# __len__
print(len(w))
# __add__
print(w + w2)
# __eq__
print(id(w))
print(id(w2))
print(w == w2)

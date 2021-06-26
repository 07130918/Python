import pickle


class T(object):

    def __init__(self, name):
        self.name = name


data = {
    'a': [1, 2, 3],
    'b': ('tpl1', 'tpl2'),
    'c': {'key': 'val'},
    'd': T('It is class')
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
    print(data_loaded['d'].name)

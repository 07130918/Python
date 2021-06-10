day_list = ['sun', 'Mon', 'Tue', 'wed', 'thu', 'Fri', 'sat']


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

# sample_func = lambda word: word.capitalize()

change_words(day_list, lambda word: word.capitalize())
print('--------------------------')
change_words(day_list, lambda word: word.lower())

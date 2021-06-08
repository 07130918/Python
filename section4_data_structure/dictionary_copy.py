kota = {'age': 21, 'fav': 'youtube'}
obito = kota
obito['fav'] = 'kamui'
print(kota)

print('----------------')

kota = {'age': 21, 'fav': 'youtube'}
obito = kota.copy()
obito['fav'] = 'kamui'
print(kota)

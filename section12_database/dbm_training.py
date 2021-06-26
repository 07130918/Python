import dbm


with dbm.open('cache', 'c') as db:
    db['key1'] = 'val1'
    db['key2'] = 'val2'

with dbm.open('cache', 'r') as db:
    print(db.get('key1'))

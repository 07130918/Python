import collections
import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first': 'Mike', 'last': 'Jackson', 'address': 'A'})
    writer.writerow({'first': 'Naruto', 'last': 'Uzumaki', 'address': 'B'})
    writer.writerow({'first': 'Sasuke', 'last': 'Uchiha', 'address': 'C'})

with open('names.csv', 'r') as f:
    csv_reader = csv.reader(f)
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        print('-' * 60)
        print(row)
        names = Names._make(row)
        print(names)
        print(names.first, names.last, names.address)

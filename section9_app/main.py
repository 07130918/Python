import csv

from termcolor import colored


def opening_greeting():
    print(colored('======================================', 'green'))
    print(colored("Hi, I'm Roboko. What is your name?", 'green'))
    print(colored('======================================', 'green'))
    return get_name()


def get_name():
    return input('Name: ')


def recommend():
    with open('ranking.csv', 'r') as csv_file:
        if len([row for row in csv.DictReader(csv_file)]) == 0:
            return
        for row in csv.DictReader(csv_file):
            print(row)
            print(row['Restaurant name'], row['Count'])


def ask_restaurant(name):
    print(colored('======================================', 'green'))
    print(colored(f"{name}, which restaurants do you like?", 'green'))
    print(colored('======================================', 'green'))
    return get_restaurant_name()


def get_restaurant_name():
    return input('Restaurant name: ')


def write_csv(restaurant_name):
    with open('ranking.csv', 'a+') as csv_file:
        fieldnames = ['Restaurant name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Restaurant name': restaurant_name, 'Count': 1})


def close_conversation(name):
    print(colored('======================================', 'green'))
    print(colored(f"Thank you so much! {name}", 'green'))
    print(colored("Have a good day!", 'green'))
    print(colored('======================================', 'green'))


def main():
    # name = opening_greeting()
    recommend()
    # restaurant_name = ask_restaurant(name)
    # write_csv(restaurant_name)
    # close_conversation(name)


if __name__ == '__main__':
    main()

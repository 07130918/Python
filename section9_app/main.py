from termcolor import colored


def opening_greeting():
    print(colored('======================================', 'green'))
    print(colored("Hi, I'm Roboko. What is your name?", 'green'))
    print(colored('======================================', 'green'))
    return get_name()


def get_name():
    return input('Name: ')


def ask_restaurant(name):
    print(colored('======================================', 'green'))
    print(colored(f"{name}, which restaurants do you like?", 'green'))
    print(colored('======================================', 'green'))
    return get_restaurant_name()


def get_restaurant_name():
    return input('Restaurant name: ')


def close_conversation(name):
    print(colored('======================================', 'green'))
    print(colored(f"Thank you so much! {name}", 'green'))
    print(colored("Have a good day!", 'green'))
    print(colored('======================================', 'green'))


def main():
    name = opening_greeting()
    ask_restaurant(name)
    close_conversation(name)


if __name__ == '__main__':
    main()

import csv

from termcolor import colored


def opening_greeting():
    print(colored('=' * 50, 'green'))
    print(colored("Hi, I'm Roboko. What is your name?", 'green'))
    print(colored('=' * 50, 'green'))


def get_name():
    return input('Name: ')


def read_csv():
    with open("ranking.csv", "r") as csv_file:
        name_count = csv.DictReader(csv_file)
        name_count_list = [i for i in name_count]
        return name_count_list


def column_to_int(name_count_list):
    for dic in name_count_list:
        for key in dic:
            if key == 'Count':
                dic[key] = int(dic[key])
    return name_count_list


def list_sort(restaurant_count):
    sorted_list = sorted(
        restaurant_count, key=lambda x: x['Count'], reverse=True)
    return sorted_list


def recommend():
    name_count_list = column_to_int(read_csv())
    sorted_list = list_sort(name_count_list)
    if len(sorted_list) == 0:
        return None
    for i in sorted_list:
        print(colored('=' * 50, 'green'))
        print(
            colored(f"I recommend {i['Restaurant name']}", 'green'))
        print(colored('Do you like it ? [y/n]', 'green'))
        yes_no = input()
        if yes_no == 'y' or yes_no == 'yes' or yes_no == 'Yes':
            i["Count"] += 1
    return sorted_list


def ask_restaurant(name):
    print(colored('=' * 50, 'green'))
    print(colored(f"{name}, which restaurants do you like?", 'green'))
    print(colored('=' * 50, 'green'))


def get_restaurant_name():
    restaurant_name = input('Restaurant name: ').title()
    return restaurant_name


def close_conversation(name):
    print(colored('=' * 50, 'green'))
    print(colored(f"Thank you so much! {name}", 'green'))
    print(colored("Have a good day!", 'green'))
    print(colored('=' * 50, 'green'))


def write_csv(ranking, restaurant_name):
    if ranking is None:
        with open('ranking.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=[
                                'Restaurant name', 'Count'])
            writer.writeheader()
            writer.writerow({'Restaurant name': restaurant_name, 'Count': 1})
    else:
        for i in ranking:
            if restaurant_name == list(i.values())[0]:
                i['Count'] += 1
                break
            else:
                ranking.append({'Restaurant name': restaurant_name, 'Count': 1})
                break
        with open('ranking.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=[
                                    'Restaurant name', 'Count'])
            writer.writeheader()
            for r in ranking:
                writer.writerow({
                    'Restaurant name': r['Restaurant name'],
                    'Count': r['Count']
                })


def main():
    opening_greeting()
    name = get_name()
    ranking = recommend()
    ask_restaurant(name)
    restaurant_name = get_restaurant_name()
    close_conversation(name)
    write_csv(ranking, restaurant_name)


if __name__ == '__main__':
    main()

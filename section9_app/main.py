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
        name_count = [i for i in name_count]
        return name_count


def column_to_int(name_count):
    for dic in name_count:
        for key in dic:
            if key == 'Count':
                dic[key] = int(dic[key])
    return name_count


def list_sort(restaurant_count):
    sorted_list = sorted(
        restaurant_count, key=lambda x: x['Count'], reverse=True)
    return sorted_list


def recommend_loop(sorted_list):
    for i in sorted_list:
        print(colored('=' * 50, 'green'))
        print(
            colored(f"I recommend {i['Restaurant name']}", 'green'))
        print(colored('Do you like it ? [y/n]', 'green'))
        yes_no = input()
        if yes_no == 'y' or yes_no == 'yes' or yes_no == 'Yes':
            i["Count"] += 1
    ranking = sorted_list
    return ranking


def counter():
    if len(read_csv()) == 0:
        return
    name_count = column_to_int(read_csv())
    sorted_list = list_sort(name_count)
    return recommend_loop(sorted_list)


def ask_restaurant(name):
    print(colored('=' * 50, 'green'))
    print(colored(f"{name}, which restaurants do you like?", 'green'))
    print(colored('=' * 50, 'green'))


def get_restaurant_name():
    return input('Restaurant name: ').title()


def close_conversation(name):
    print(colored('=' * 50, 'green'))
    print(colored(f"Thank you so much! {name}", 'green'))
    print(colored("Have a good day!", 'green'))
    print(colored('=' * 50, 'green'))


def create_new_csv(restaurant_name):
    with open('ranking.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[
            'Restaurant name', 'Count'])
        writer.writeheader()
        writer.writerow({'Restaurant name': restaurant_name, 'Count': 1})


def write_csv(ranking, restaurant_name):
    if len(read_csv()) == 0:
        create_new_csv(restaurant_name)
        return

    through_status = None
    for i in ranking:
        if restaurant_name == list(i.values())[0]:
            through_status = 'ok'
            i['Count'] += 1
            break
    if through_status != 'ok':
        ranking.append({'Restaurant name': restaurant_name, 'Count': 1})

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
    ranking = counter()
    ask_restaurant(name)
    restaurant_name = get_restaurant_name()
    close_conversation(name)
    write_csv(ranking, restaurant_name)


if __name__ == '__main__':
    main()

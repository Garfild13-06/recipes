import os
from pprint import pprint

full_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(full_path, 'rt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingridients_count = int(file.readline().strip())
        ingridients = []
        for _ in range(ingridients_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingridients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingridients


# pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            shop_list[ingridient['ingredient_name']] = {
                'measure': ingridient['measure'],
                'quantity': (int(ingridient['quantity']) * person_count)
            }
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def task_3():
    files_len = {}
    for i in range(1, 4):
        path = os.path.join(os.getcwd(), 'files', f'{i}.txt')
        with open(path, 'rt') as file:
            content = file.readlines()
            files_len[len(content)] = f"{i}.txt"

    res_file_path = os.path.join(os.getcwd(), 'files', 'result.txt')
    result_str = ""
    for file in sorted(files_len):
        path = os.path.join(os.getcwd(), 'files', files_len[file])
        with open(path, 'rt') as f:
            result_str += f"{files_len[file]}\n"
            file_num = files_len[file].split('.')[0]
            for index, line in enumerate(f):
                result_str += f"Строка номер {index + 1} файла {file_num}\n"
                result_str += f"{line.strip()}\n"
    if os.path.exists(res_file_path):
        os.remove(res_file_path)
        with open(res_file_path, 'xt', encoding='utf-8') as f:
            f.write(result_str)
    else:
        with open(res_file_path, 'xt', encoding='utf-8') as f:
            f.write(result_str)


task_3()

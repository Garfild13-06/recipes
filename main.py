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

pprint(cook_book, sort_dicts=False)

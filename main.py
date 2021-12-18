def generate_cook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as file:

        for line in file:
            if line == '\n':
                continue
            else:
                list = []
                dish_name = line.strip()
                count = int(file.readline().strip())
                for numb in range(0, count):
                    product_list = file.readline().split(' | ')
                    dict = {'ingredient_name': product_list[0], 'quantity': product_list[1],
                            'measure': product_list[2].strip()}
                    list.append(dict)
                cook_book[dish_name] = list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = generate_cook_book()
    ingredient_value = {}
    for dish in dishes:
        if dish in cook_book.keys():
            ingredients_list = cook_book.get(dish)
            for ingredient in ingredients_list:
                ingredient_name = ingredient.pop('ingredient_name')
                if ingredient_name in ingredient_value.keys():
                    ingredient['quantity'] = int(ingredient['quantity']) * 2
                    ingredient_value[ingredient_name] = ingredient
                else:
                    ingredient_value[ingredient_name] = ingredient
    for value in ingredient_value.values():
        value['quantity'] = int(value['quantity']) * 2
    return ingredient_value


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
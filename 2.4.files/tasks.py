with open('recipes.txt', encoding='utf-8') as f:
    cook_book = []
    for l in f:
        dish_name = l.strip()
        ingridients_count = int(f.readline())
        ingridients = []
        for _ in range(ingridients_count):
            ing = f.readline().split(' | ')
            name, amount, measure = ing
            ingridients.append({'ingridient_name': name,
                                'quantity': amount,
                                'measure': measure})
        f.readline()
        cook = {f'{dish_name}': ingridients}
        cook_book.append(cook)

print(cook_book)
#не понимаю, как сделать правильный формат в 1ом задании (cook_book - список, а не словарь) и поэтому не получается сделать 2ое задание. Помогите, пожалуйста :(

# def get_shop_list_by_dishes(dishes, person_count):
#     result = []
#     dish = cook_book[f'dishes']
#     print(dish)
#
# get_shop_list_by_dishes('Запеченый картофель', 2)


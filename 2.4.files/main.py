import os

with open('recipes.txt', encoding='utf-8') as f:
    count = f.readlines().count('\n') + 1

my_dict = []

with open('recipes.txt', encoding='utf-8') as f:
    ingridients = []
    dishes = []
    for i in range(count):
        dish = f.readline()
        dishes.append(dish)
        count_ing = int(f.readline())

        for i in range(count_ing):
            ingridient = f.readline().split(' | ')
            ing = {'ingredient_name': ingridient[0],
                   'quantity': ingridient[1],
                   'measure': ingridient[2]}
            ingridients.append(ing)
        f.readline()
        my_dict.append(ingridients)

cook_book = {
    f'{dishes[0]}': my_dict[0],
    f'{dishes[1]}': my_dict[1],
    f'{dishes[2]}': my_dict[2],
    f'{dishes[3]}': my_dict[3]
}

print(cook_book)
# print(cook_book['Омлет\n'])

def get_shop_list_by_dishes(dishes1, person=1):
    shop_list = []
    for dish1 in dishes1:
        if dish1 in cook_book.keys():
            for values in cook_book[dish1]:
                ing2 = [values['ingredient_name'], values['measure'], values['quantity']]
                shop_list.append(ing2)
    print(shop_list)

get_shop_list_by_dishes(['Омлет\n'])

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }


#задание 3
print(os.getcwd())
# C:\Users\Варвара\Desktop\Новая папка\py-homework-basic-files\2.4.files\sorted\'1.txt'
with open('sorted\1.txt') as f1:
    count1 =int(f1.readlines())

with open('2.txt') as f2:
    count2 = int(f2.readlines())

with open('3.txt') as f3:
    count3 = int(f3.readlines())

if count1 < count2 and count1 < count3:
    print('1.txt')
    if count3 < count2:
        print('3.txt')
        print('2.txt')
    else:
        print('2.txt')
        print('3.txt')
elif count2 < count1 and count2 < count3:
    print('2.txt')
    if count3 < count1:
        print('3.txt')
        print('1.txt')
    else:
        print('1.txt')
        print('3.txt')
else:
    print('3.txt')
    if count1 < count2:
        print('1.txt')
        print('2.txt')
    else:
        print('2.txt')
        print('1.txt')


# #как избавиться от '\n' в 1ом задании?
# почему в шоп листе ингредиенты всех блюд?
# почему не получается прописать правильный путь к файлу?
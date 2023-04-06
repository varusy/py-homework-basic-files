with open('recipes.txt', encoding='utf-8') as f:
    dish = f.readline()
    count_ing = int(f.readline())
    ingridients = []
    for i in range(count_ing):
        ingridient = f.readline().split()
        ing = {'ingredient_name': ingridient[0],
               'quantity': ingridient[1],
               'measure': ingridient[2]}
        ingridients.append(ing)

print(ingridients)
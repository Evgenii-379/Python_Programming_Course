
def read_cookbook(filename):
    cook_book = {}

    with open(filename, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()

            if line == "":
                break

            dish_name = line.strip()

            if dish_name == "":
                continue

            ingredient_count = int(file.readline().strip())


            ingredients = []

            for i in range(ingredient_count):
                ingredient_line = file.readline().strip()
                parts = ingredient_line.split("|")
                ingredient_name = parts[0].strip()
                quantity = int(parts[1].strip())
                measure = parts[2].strip()



                ingredient = {
                    "ingredient_name": ingredient_name,
                    "quantity": quantity,
                    "measure": measure
                }

                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients

        return cook_book

cook_book = read_cookbook("cookbook.txt")
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        ingredients = cook_book[dish]

        for ingr in ingredients:
            name = ingr["ingredient_name"]
            quantity = ingr["quantity"]
            measure = ingr["measure"]

            total_quantity = quantity * person_count

            if name in shop_list:
                shop_list[name]["quantity"] += total_quantity
            else:
                shop_list[name] = {
                    "measure": measure,
                    "quantity": total_quantity
                }

    return shop_list

shopping_list = get_shop_list_by_dishes(["Омлет", "Фахитос"], 2, cook_book)

print(shopping_list)











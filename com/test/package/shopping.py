shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    print(item)

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy "  + item)

for item in shopping_list:
    if item == "spam":
        print("break "  + item)
        break

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("Item is found at {}".format(found_at))
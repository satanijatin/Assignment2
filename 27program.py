
my_tuple = (1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 9, 9)


repeated_items = set()
unique_items = set()


for item in my_tuple:
    if item in unique_items:
        repeated_items.add(item)
    else:
        unique_items.add(item)


print("Original Tuple:", my_tuple)
print("Repeated Items:", repeated_items)

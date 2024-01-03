import random

def select_random_item(my_list):
    if not my_list:
        return None  
    else:
        return random.choice(my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_item = select_random_item(my_list)

print("Randomly selected item: ",random_item)

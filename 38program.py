my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
keys_to_check = ['a', 'c', 'f']

for key in keys_to_check:
    if key in my_dict:
        print(f"Key '{key}' exists in the dictionary with value: {my_dict[key]}")
    else:
        print(f"Key '{key}' does not exist in the dictionary")


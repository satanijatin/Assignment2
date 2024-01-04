
my_dictionary = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}

unique_values = set()

for value in my_dictionary.values():
    unique_values.add(value)

print("Unique values in the dictionary:", list(unique_values))

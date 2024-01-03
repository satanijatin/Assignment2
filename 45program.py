def find_highest_values(dictionary, n=3):
    sorted_values = sorted(dictionary.values(), reverse=True)
    highest_values = sorted_values[:n]
    return highest_values

my_dict = {'a': 10, 'b': 25, 'c': 15, 'd': 30, 'e': 20}
highest_values = find_highest_values(my_dict, 3)

print("Original Dictionary:", my_dict)
print("Highest 3 values:", highest_values)

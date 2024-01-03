my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

ascending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))


descending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Order by Values:", ascending_sorted_dict)
print("Descending Order by Values:", descending_sorted_dict)

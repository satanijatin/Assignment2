
original_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10

updated_list = [(t[:-1] + (new_value,)) for t in original_list]

print("Original List:", original_list)
print("Updated List:", updated_list)


list_of_tuples = [(1, 2), (), (3, 4), (), (5, 6), (), (), (7, 8)]


filtered_list = []
for tpl in list_of_tuples:
    if tpl:
        filtered_list.append(tpl)

print("Original List of Tuples:", list_of_tuples)
print("List after Removing Empty Tuples:", filtered_list)

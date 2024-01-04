from collections import Counter

def combine_dicts(d1, d2):
  
    combined_counter = Counter(d1) + Counter(d2)
    return combined_counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_result = combine_dicts(d1, d2)
print("Combined Result:", combined_result)

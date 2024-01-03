from collections import Counter

def combine_values(list_of_dicts):
    result_counter = Counter()

    for d in list_of_dicts:
        item = d['item']
        amount = d['amount']
        result_counter[item] += amount

    return result_counter

sample_data = [{'item': 'item1', 'amount': 400},
               {'item': 'item2', 'amount': 300},
               {'item': 'item1', 'amount': 750}]


result = combine_values(sample_data)


print(result)

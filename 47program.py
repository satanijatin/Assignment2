def create_dictionary_from_string(input_string):
    result_dict = {}

    for char in input_string:
        if char in result_dict:
            result_dict[char] += 1
        else:
            result_dict[char] = 1

    return result_dict

sample_string = 'w3resource'

result = create_dictionary_from_string(sample_string)

print(result)

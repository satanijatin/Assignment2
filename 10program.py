
# squares_list = [i**2 for i in range(1, 31)]
# print("First 5 elements:", squares_list[:5])
# print("Last 5 elements:", squares_list[-5:])

def rearrange_list(lst):
    for i in range(1, len(lst), 2):
        print( lst[i], lst[i-1])
        print( lst[i-1], lst[i])
        lst[i], lst[i-1] = lst[i-1], lst[i]
    return lst

# Test the function
input_list = [5, 10, 5, 12, 13, 14]
output_list = rearrange_list(input_list)
print(output_list)

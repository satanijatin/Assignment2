decimal_numbers = [7.89,8.59,3.14, 2.71, 1.618, 0.4, 2.0]
max_number = min_number = decimal_numbers[0]

for num in decimal_numbers[1:]:
    if num > max_number:
        max_number = num
    elif num < min_number:
        min_number = num

print("Maximum number: ",max_number)
print("Minimum number:", min_number)

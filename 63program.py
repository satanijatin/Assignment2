user_input = int(input("Enter a positive integer: "))


if user_input <= 0:
    print("Please enter a positive integer.")
else:
    divisor_sum = 0

   
    for i in range(1, user_input + 1):
       
        if user_input % i == 0:
            divisor_sum += i

 
    print(divisor_sum)

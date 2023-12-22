
base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))


if base <= 0 or height <= 0:
    print("Please enter positive values for base and height.")
else:
   
    area = base * height
 
    print("The area of the parallelogram is: ",area)

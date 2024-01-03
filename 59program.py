import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees_value = float(input("Enter degrees: "))

radians_value = degrees_to_radians(degrees_value)

print(f"{degrees_value} degrees is equal to {radians_value} radians.")

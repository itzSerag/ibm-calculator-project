
# FIXED PRICE
WEIGHT = 20
DISTANCE = 50

print("Welcome to the Super Calculator!")
print("This calculator will help you calculate the cost of your trip.")
weight = float(input("Please enter the weight of your package in kg:"))
distance = float(input("Please enter the distance of your trip in km:"))

cost = (weight * WEIGHT) + (distance * DISTANCE)
print(f"The cost of your trip is: {cost} dollars.")
print("Thank you for using the Super Calculator!")
print("Goodbye!")



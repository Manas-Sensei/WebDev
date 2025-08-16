# BMI Calculator
# This program calculates the Body Mass Index (BMI) based on user input for weight and height
Height = input("Enter your height in meters: ")
Weight = input("Enter your weight in kilograms: ")
height = float(Height)
weight = float(Weight)
if height <= 0 or weight <= 0:
    print("Height and weight must be positive numbers.")
else:
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
reduce_weight = weight - (24.9 * (height ** 2))
if reduce_weight > 0:
    print(f"You need to lose {reduce_weight:.2f} kg to reach a normal weight.")
else:
    print("You are already at a normal weight")

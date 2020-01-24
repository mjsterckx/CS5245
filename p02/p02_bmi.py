height = float(input("Enter height in inches: "))
weight = float(input("Enter weight in pounds: "))
bmi = 703 * (weight / (height ** 2))
category = "obese"
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "healthy"
elif bmi < 30:
    category = "overweight"
print("The BMI is " + str(bmi) + " which is considered to be " + category + ".")

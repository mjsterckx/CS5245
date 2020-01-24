sex = input("Enter sex (M or F): ")
body_fat = float(input("Enter the body fat percentage: "))
classification = "Deficient"
if sex == "M":
    if body_fat >= 25:
        classification = "Obese"
    elif body_fat >= 18:
        classification = "Average"
    elif body_fat >= 14:
        classification = "Fitness"
    elif body_fat >= 6:
        classification = "Athletes"
    elif body_fat >= 2:
        classification = "Essential fat"
elif sex == "F":
    if body_fat >= 32:
        classification = "Obese"
    elif body_fat >= 25:
        classification = "Average"
    elif body_fat >= 21:
        classification = "Fitness"
    elif body_fat >= 14:
        classification = "Athletes"
    elif body_fat >= 10:
        classification = "Essential fat"
print(str(body_fat) + "% body fat for a " + sex + " is considered " + classification + ".")

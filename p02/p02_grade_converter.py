score = float(input("Enter the score: "))
letter_grade = "invalid"
if score > 100:
    letter_grade = "invalid"
elif score >= 90:
    letter_grade = "A"
elif score >= 80:
    letter_grade = "B"
elif score >= 70:
    letter_grade = "C"
elif score >= 60:
    letter_grade = "D"
elif score >= 0:
    letter_grade = "F"
print("The score is " + str(score) + " and the letter grade is " + letter_grade + ".")

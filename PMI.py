def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi)

print("BMI:", bmi)
print("Interpretation:", interpretation)
print("File is running")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

weight = 60
height = 1.65

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")

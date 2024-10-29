def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    bmi = weight / (height * height)

    print("BMI=" + str(bmi))

    if bmi < 18.5:
        classification = "Under Weight"
        return bmi, classification, -1
    if 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
        return bmi, classification, 0
    else:
        classification = "Over Weight"
        return bmi, classification, 1


bmi_value, classification, return_value = calculate_bmi(weight=40, height=1.73)
print(f"BMI Value: {bmi_value}, Classification: {classification}, Return Value: {return_value}")

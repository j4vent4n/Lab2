def calculate_bmi(height,weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))


    bmi = weight/ (height * height )

    print("BMI="+str(bmi))

    if bmi < 18.5 :
        print("Weight Classification: Under Weight")
    if 18.5 <= bmi <= 25.0:
        print("Weight Classification: Normal Weight")
    if bmi > 25:
        print("Weight Classification: Over Weight")

 


calculate_bmi(weight=40,height=1.73)


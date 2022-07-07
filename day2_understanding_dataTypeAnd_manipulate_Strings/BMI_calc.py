# if BMI < 18.5 = underweght
# if BMI > 18.5 and <25 = normal weight
# between 25 and 30 = overweight
# between 30 and 35 = obese
# > 35 = critically obese

from re import L


def userInput():
    height = input("Enter your height(m): ")
    weight = input("Enter weight(kg): ")

    return height,weight


def height(value):
    height = float(value[0])

    return height


def weight(value):
    weight = float(value[1])

    return weight


def bmi(weight_, height_):
    result = (weight_)/(height_**2)

    return result

    
def bmiStatus(bmi):

    if bmi < 18.5:
        status = "underweight"

    elif bmi < 25:
        status = "normal weight"

    elif bmi < 30:
        status = "overweight"

    elif bmi < 35:
        status = "obese"

    else:
        status =  "critically obese"

    return status


if __name__ == "__main__":
    input_ = userInput()
    height_ = height(input_)
    weight_ = weight(input_)
    result = bmi(weight_,height_)
    weightStatus = bmiStatus(result)
    print("Your body mass index (BMI) is: {} you are {}.".format(round(result), weightStatus))
    
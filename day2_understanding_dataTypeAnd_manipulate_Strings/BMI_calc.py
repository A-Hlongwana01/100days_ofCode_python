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

    
if __name__ == "__main__":
    input_ = userInput()
    height_ = height(input_)
    weight_ = weight(input_)
    result = bmi(weight_,height_)
    print("Your body mass index (BMI) is: {}".format(round(result)))
    
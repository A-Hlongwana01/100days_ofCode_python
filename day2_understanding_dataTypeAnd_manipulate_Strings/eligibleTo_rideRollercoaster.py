#  if height is greater than 120cm, then one is eligible to ride
# if ones age is > 18, they will pay  $12
# if age is <= 18, they pay $7
def userHeight():
    height = float(input("Enter your height in cm: ")); return height


def userAge():
    age = int(input("Enter your age: ")); return age


def accessEvaluator(height, age):
    if height > 120:
        if age <= 18:
            print("You will pay $7 for the ride")
        else:
            print("You will pay $12 for the ride")
    else:
        print("Not eligible to ride")

if __name__=="__main__":
    height = userHeight()
    age = userAge()
    accessEvaluator(height, age)


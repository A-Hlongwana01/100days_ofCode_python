def userInput():
    number = int(input("Enter a number:"))
    return number


def evaluator(number):
    if number % 2 == 0:
        return "This is an even number"
    else:
        return "This is an odd number"

if __name__== "__main__":
    num = userInput()
    result = evaluator(num)
    print(result)
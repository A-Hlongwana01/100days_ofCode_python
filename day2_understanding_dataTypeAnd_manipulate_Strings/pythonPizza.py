# pizza sizes:
#   Small('S'): $15
#   Medium('M'): $20
#   Large('L'): $25
# Add-ons:
#   Pepporoni for small pizza: +$2
#   Pepperoni for medium or large pizza: +$3
#   
#   Extra cheese for any size pizza: +$1
def welcome():
    print("Welcome to Python Pizza Deliveries!")


def pizzaSize():
    answer = input("What size pizza do you want? S, M, or L ? "); return answer.upper()


def addPepperoni():
    answer = input("Do you want pepperoni? Y on N ? "); return answer.upper()


def addExtraCheese():
    answer = input("Do you want extra cheese? Y, or N ? "); return answer.upper()


def priceEvaluator(size, addPepperoni, addCheese)-> float:
    pizzaPrice = 0
    pepperoniPrice = 0
    cheesePrice = 0

    if size == 'L':
        pizzaPrice = 25
        if addPepperoni == 'Y':
            pepperoniPrice = 3
        if addCheese == 'Y':
            cheesePrice = 1
    elif size == 'M':
        if addPepperoni == 'Y':
            pizzaPrice = 20
            pepperoniPrice = 3
        if addCheese == 'Y':
            cheesePrice = 1
    elif size == 'S':
        pizzaPrice = 15
        pepperoniPrice = 2
        if addCheese == 'Y':
            cheesePrice = 1
    
    return pizzaPrice+pepperoniPrice+cheesePrice
    

def finalBill(price):
    print("Your final bill is ${:.2f}.".format(price))


if __name__=="__main__":
    welcome()
    size = pizzaSize()
    addPepp = addPepperoni()
    addCheese = addExtraCheese()
    price = priceEvaluator(size,addPepperoni,addCheese)
    finalBill(price)
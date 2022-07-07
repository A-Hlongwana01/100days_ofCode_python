def welcome_message()-> str:
    print("Welcome to the tip calculator.")


def totalBill():
    bill = float(input("What was the total bill? $")); return bill


def noPeopleTo_splitBill():
    noPeople = int(input("How many people to split the bill? ")); return noPeople


def billRate():
    rate = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    rate/=100; return round(rate, 2)


def tipCalc(totalBill, rate) -> float:
    tip = totalBill*rate; return tip


def totalIncludTip(totalBill, tip):
    toBe_payed = totalBill+tip; return toBe_payed


def splitBill(totalBill_plusTip, noPeopleTo_splitBill) ->float:
    splitted = totalBill_plusTip/noPeopleTo_splitBill; return splitted


def print_message(split_amount, totalIncBill)-> str:
    if split_amount == totalIncBill:
        print("You should pay: ${:.2f}".format(totalIncBill))
    else: 
        print("Each person should pay: ${:.2f}".format(split_amount))


if __name__== "__main__":
    welcome_message()
    billTotal = totalBill()
    rate = billRate()
    noPeople = noPeopleTo_splitBill()
    tip_ = tipCalc(billTotal, rate)
    totalWith_Tip = totalIncludTip(billTotal, tip_)
    splitAmount = splitBill(totalWith_Tip, noPeople)
    print_message(splitAmount,totalWith_Tip)
    





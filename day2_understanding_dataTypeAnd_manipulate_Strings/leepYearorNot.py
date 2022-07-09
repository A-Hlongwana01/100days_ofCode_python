def yearInput():
    year = int(input("Enter year you want to check: "))
    return year


def isLeapYear(year):

    if year % 4 != 0:
        leapYear = False
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                leapYear = True
            else:
                leapYear = False
        else:
            leapYear = True

    return leapYear


def result(isLeapYear)-> str:
    if isLeapYear:
        return "a leap year"
    else:
        return "not a leap year"
        

def printResult(year,result):
    print("{} is {}".format(year, result))

if __name__=="__main__":
    yearTocheck = yearInput()
    isLeap_orNot = isLeapYear(yearTocheck)
    a = result(isLeap_orNot)
    printResult(yearTocheck, a)


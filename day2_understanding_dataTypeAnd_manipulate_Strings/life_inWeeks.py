# 1yr = 365 days
# 1yr = 52 weeks
# 1yr = 12 months

def userInput():
    years = int(input("Enter age(yrs): "));return years


def ageIn_months(years):
    months = years*12;return months


def ageIn_weeks(years):
    weeks = years*52;return weeks


def ageIn_days(years):
    days = years*365;return days


def age(years):
    # years = userInput()
    months = int(ageIn_months(years))
    weeks = int(ageIn_weeks(years))
    days = int(ageIn_days(years))

    return months,weeks,days

def lifeLeft(age):
    maxYearsToLive = 90
    ages = []

    for i in age:
        if i % 12 == 0:
            timeLeftToDie = (maxYearsToLive*12)-i
            ages.append(timeLeftToDie)

        if i % 52 == 0:
            timeLeftToDie = (maxYearsToLive*52)-i
            ages.append(timeLeftToDie)

        if i % 365 == 0:
            timeLeftToDie = (maxYearsToLive*365)-i
            ages.append(timeLeftToDie)

    return ages


def main():
    years = userInput()
    agesInMMWWDD = age(years)
    timeLeftList = lifeLeft(agesInMMWWDD)
    months = timeLeftList[0]
    weeks = timeLeftList[1]
    days = timeLeftList[2]
    
    return "You have {} days, {} weeks, and {} months left.".format(days,weeks,months)

    
    
if __name__ == "__main__":


    # 24 ->12
    # maxYearsToLive = 90
    # ages = []
    # ageTuple = {120,520,3650}
    # equals_oneYear = [12,52,365]
    # for index in ageTuple:
    #     i = 0
    #     for year in equals_oneYear:

    #         if index % equals_oneYear == 0:
    #             timeLeftToDie = ((maxYearsToLive*equals_oneYear[i])-index)
    #             ages.append(timeLeftToDie)
    #     i+=1
    
    # print(ages)
    print(main())
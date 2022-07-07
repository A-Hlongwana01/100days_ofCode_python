# print(10*12)
# print(10*52)
# print(10*365 )

print("120 % 12     :{}".format(120%12))
print("120 % 52     :{}".format(120%52))
print("120 % 365    :{}\n".format(120%365))

print("520 % 12     :{}".format(520%12))
print("520 % 52     :{}".format(520%52))
print("520 % 365    :{} \n".format(520%365))

print("3650 % 12    :{}".format(3650%12))
print("3650 % 52    :{}".format(3650%52))
print("3650 % 365   :{}".format(3650%365))


def lifeLeft(age):
    maxYearsToLive = 90
    ages = []

    for i in age:
        if i % 12 == 0:

            timeLeftToDie = (maxYearsToLive*12)-(i)
            ages.append(timeLeftToDie)

        if i % 52 == 0:
            timeLeftToDie = (maxYearsToLive*52)-i
            ages.append(timeLeftToDie)

        if i % 365 == 0:
            timeLeftToDie = (maxYearsToLive*365)-i
            ages.append(timeLeftToDie)
    return ages

print(lifeLeft({672,2912,20440}))
print(120/12)
print(520/52)
print(3650/365)

print(56*12)

print(56*52)

print(56*365)

print("139.5072 / 7 = {}".format(139.5072/7))

# ################################

print("leap year")
print("1989%4: {}".format(2400%4))
print("1989%100: {}".format(2400%100))
print("1989%400: {}".format(2400%400))



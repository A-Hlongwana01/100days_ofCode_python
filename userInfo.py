def getName():
    with open("name.txt", 'r') as info:
        a = info.readlines()

    # listy = a[0].split("name: ")
    # x = listy[1]
    # y = x.split()
    # name = y[0]
    return a


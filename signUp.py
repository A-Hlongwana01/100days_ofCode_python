import random


def firstName():
    while True:
        name = input("First name: ")
        if name.isalpha() == False:
            print("Oops!! that is not a valid name \nPlease try again")
            continue
        else:
            break
    return name
        

def lastName():
    while True:
        name = input("Last name: "); 
        if name.isalpha() == False:
            print("Oops!! that is not a valid name \nPlease try again")
            continue
        else:
            break
    return name


def userName(fname, lname):
    nums = ''
    for i in range(3):
        j = random.randint(0,9)
        nums+=str(j)
    if len(lname) >= 7:
        lname = lname[:7]
    userName = fname[:2]+lname+nums
    print(userName.lower())


fname = firstName()
lname = lastName()
userName(fname,lname)
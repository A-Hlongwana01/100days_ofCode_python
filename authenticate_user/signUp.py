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
    for i in range(4):
        j = random.randint(0,9)
        nums+=str(j)
    if len(lname) >= 7:
        lname = lname[:7]
    userName = fname[:2]+lname+nums
    return userName.lower()


def passwd() -> str:
    password = input("Enter password: ")
    return password


def getCredentials(userName, password):
    creds = []
    creds.append(userName)
    creds.append(password)
    return creds


def run():
    fname = firstName()
    lname = lastName()
    user_name = userName(fname,lname)
    password = passwd()
    x = getCredentials(user_name, password)
    return x
 
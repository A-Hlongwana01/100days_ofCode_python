from authenticate_user.signUp import run


def userName():
    user_name  = input("Enter user name: ")
    return user_name


def passwd():
    password = input("Enter password: ")
    return password


def getCredentials(userName, password):
    creds = []
    creds.append(userName)
    creds.append(password)
    return creds

def run():
    user_name = userName()
    password = passwd()
    x = getCredentials(user_name, password)
    return x

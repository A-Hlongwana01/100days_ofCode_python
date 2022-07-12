from operator import index
import userInfo
#  check if user_name in usernames stored in data

def userNameExist(username):
    if username in userInfo.userNames():
        print("Yess!!!!")
        return username
    else:
        print("Ooops!!!!! username does not exist")
        return False


# checks if password is in existing passwords
def passwordExist(password):
    if password in userInfo.userPasswords():
        return password
    else:
        return False


# check if given username and password match (in same indexes of list)
def match(username_exists, password_exists):
    if type(username_exists) != bool and type(password_exists) != bool:
        passIndex = userInfo.userPasswords().index(password_exists)
        userIndex = userInfo.userNames().index(username_exists)

        if passIndex == userIndex:
            print("Access granted")
            return True


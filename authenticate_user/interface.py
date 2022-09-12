def greeting():
    print("Hello there")


def loginOrSignup():
    while True:
        loginSignup = input("\nLogin(l) or Signup(s)?")
        if loginSignup.lower() == "l":
            print("Okay...")
            return "l"
            break
        elif loginSignup.lower() == "s":
            print("Okay...")
            return "s"
            break
        else:
            print("\nOoops!\nchoose between 'l'(login) and 's'(signup)")
            continue

greeting()
loginOrSignup()

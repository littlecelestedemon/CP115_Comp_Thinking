#a set number of users and their passwords are already defined beforehand
#the first input asks if the person is a returning user
#if they are not a returning user, it skips down to establishing a new name and password
#checking of course for existing users
#is they already are in the system, the program prompts you to enter the correct
#login and password
#the "existing" users are me and my dogs

print("Write loginRun() to start this program")

def loginRun():

    Wusername = "Willa"
    Lusername = "Luna"
    Rusername = "Roscoe"
    Wpassword = "GraphicDesign"
    Lpassword = "DinnerTime"
    Rpassword = "RunandJump"

    neworexisting = input("Are you a returning user? If yes, print y, if no, print n")

    if (neworexisting == "y"):
        qusername = input("What is your username?")
        if (qusername == Wusername):
            qpassword = input("What is your password, Willa?")
            if(qpassword == Wpassword):
                print("Login Successful! Welcome back, Willa.")
            else:
                print("Invalid Login")
        elif (qusername == Lusername):
            qpassword = input("What is your password, Luna?")
            if(qpassword == Lpassword):
                print("Login Successful! Welcome back, Luna.")
            else:
                print("Invalid Login")
        elif (qusername == Rusername):
            qpassword = input("What is your password, Roscoe?")
            if(qpassword == Rpassword):
                print("Login Successful! Welcome back, Roscoe.")
            else:
                print("Invalid Login")
        else:
            print("User cannot be found.")
    elif (neworexisting == "n"):
        newname = input("Please input a new username:")
        if(newname == Wusername or newname == Lusername or newname == Rusername):
            print("That username is already taken.")
        else:
            newpassword = input("Please input a password:")
            print("Welcome, " + newname)
    else:
        print("Invalid Choice")

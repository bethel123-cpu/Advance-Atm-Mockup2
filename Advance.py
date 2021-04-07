# register

# login

# Initializing the system....
import random
import datetime

DataBase = {}  # Datatype --> dictionary


def init():

    isValidOption = False
    print('Welcome to Ogbuji Mortgage Bank')

    while isValidOption == False:
        EnterAccount = int(
            input("Do you have an account with us: 1. (YES) 2. (NO) \n"))

        if (EnterAccount == 1):
            isValidOption = True
            login()
        elif(EnterAccount == 2):
            isValidOption = True
            print(register())
        else:
            print("Your have selected an invalid option!")


def login():
    print('-----> Login to your Account <-----')

    AccountNOfromUser = int(input("Enter your Account Number...,\n"))
    password = input("What is your password \n")

    for AccountNO, UserDetails, in DataBase.items():
        if (AccountNO == AccountNOfromUser):
            if(UserDetails[3] == password):
                bankoperations(UserDetails)

    print("Invalid Account Number or password")
    login()


def register():

    CreateAccount = int(input(
        'Do you want to create an Account with us?.. 1.(Yes) 2.(No)\n'))
    print('-----> Register Now <-----')
    print('Please fill the required inputs...')

    if (CreateAccount == 1):
        inp = "Input"
        email = input(f'{inp} Your email....\n')
        Firstname = input(f'{inp} Your First name...\n')
        Lastname = input(f'{inp} Your Lastname (*Surname)\n')
        password = input('Create Password \n')

        AccountNO = generateAccountNO()

        DataBase[AccountNO] = [Firstname, Lastname, email, password]

        print('-----> Your Account has been Activated Successfully. <----- ')
        print(' <<<<<< --------- >>>>>')
        print('Your Account number is %d' % AccountNO)
        print('<<<<<< ---------- >>>>>')
        print("Make sure you copy and Keep it safe.")
        print('<<<<<< ---------- >>>>>')

        login()

    elif (CreateAccount == 2):
        init()
    else:
        print("invalid Value input!..")


def bankoperations(User):
    print('Welcome %s %s' % (User[0], User[1]))

    Selectedoption = int(
        input("What do you want to do? (1) Withdraw (2) Deposit (3)Complaint (4)Logout (5)Exit \n"))

    if(Selectedoption == 1):
        WithdrawalOperations()

    elif(Selectedoption == 2):
        DepositOperations()

    elif(Selectedoption == 3):
        Complaint()

    elif(Selectedoption == 4):
        Logout()

    elif(Selectedoption == 5):
        exit()

    else:
        print("Invalid Value selected! Try again")
        bankoperations(User)


def WithdrawalOperations():
    withdraw = int(input("Enter (1) For withdrawal 0r (2) For Logout \n"))
    if(withdraw == 1):
        Naira = "N"
        Cashout = int(input("Enter the amount you want?? \n"))
        print("Transaction in progress------>>>> \n")
        Print('Successful..... \n')
        print("Take you cash!..%s%d" % (Naira, Cashout))
        import datetime

        now = datetime.datetime.now()
        print('current date and time:')
        print(now.strftime("%Y-%m-%d  %H:%M:%S"))
        print('<<<<<< ---------- >>>>>')

        Going = False
        while Going == False:
            chooos = int(input("Enter (1)Logout or (2)Exit \n"))
            if(chooos == 1):
                Going = True
                Logout()
            elif(chooos == 2):
                Going = True
                exit()
            else:
                print("Invalid operation.. Try again!")

    elif(withdraw == 2):
        Logout()

    else:
        print("Invalid input entered, Please try again!")


def DepositOperations():
    Naira = "N"
    Depo = int(input("Enter (1) For Depositing 0r (2) For Logout \n"))
    if(Depo == 1):
        Donate = int(input("how much do you want to deposit?? \n"))
        print("Transaction Successful..")
        print('Your current balance is:  %s%d' % (Naira, Donate))
        import datetime

        now = datetime.datetime.now()
        print('current date and time:')
        print(now.strftime("%Y-%m-%d  %H:%M:%S"))
        print('<<<<<< ---------- >>>>>')
        Going = False
        while Going == False:
            chooos = int(input("Enter (1)Logout or (2)Exit \n"))
            if(chooos == 1):
                Going = True
                Logout()
            elif(chooos == 2):
                Going = True
                exit()
            else:
                print("Invalid operation.. Try again!")

    elif(Depo == 2):
        Logout()
    else:
        print("Invalid input entered..")


def generateAccountNO():
    return random.randrange(1111111111, 9999999999)


def Complaint():
    ChooseOption = int(input("Enter (1) For Complaints 0r (2) For Logout \n"))
    if (ChooseOption == 1):
        print(input('What are your complaints??.. pls state them! \n'))
        print('Thanks for your patience, We will see to your plights soon... \n')
        import datetime

        now = datetime.datetime.now()
        print('current date and time:')
        print(now.strftime("%Y-%m-%d  %H:%M:%S"))
        print('<<<<<< ---------- >>>>>')

        Going = False
        while Going == False:
            chooos = int(input("Enter (1)Logout or (2)Exit \n"))
            if(chooos == 1):
                Going = True
                Logout()
            elif(chooos == 2):
                Going = True
                exit()
            else:
                print("Invalid operation.. Try again!")

    elif(ChooseOption == 2):
        Logout()
    else:
        print("Invalid Input entered, Try again!!")
        Complaint()


def Logout():
    login()


##### Actual Operational Activity #####
# print(generateAccountNO())
init()

import datetime


class ChooseOption:
    @staticmethod
    def welcome():
        print("Welcome to.. \nSea-Shore Super market;")  # landing output
        print('....Easy buy in better rate!')
        print("=" * 30)

        now = datetime.datetime.now()
        print('The time is:')
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

        print("=" * 30)
        print('We have Food items and Cloths remaining in the store! \nThere are also some Entertaining events')

        print("=" * 30)

        # The class direct is on line 220 , view to understand my code
        direct.direct_Selected()


class Depositing:
    @staticmethod
    def Deposite():
        chose = int(input(
            ("What Budget are you depositing for:\n(1) Food\n(2) Clothing\n(3) Entertainment\n")))
        if (chose == 1):
            return Budget().food()
        elif(chose == 2):
            return Budget().cloths()
        elif(chose == 3):
            return Budget().Entertain()
        else:
            print('Invalid input entered, Try again!')
            Depositing().Deposite()


# my dictionary collecting the funds # i just stated this dictionary but i didnt use it at all...
DataBase = {}


class Budget:
    @classmethod
    def food(cls):
        print('User you chose Food')
        print("=" * 30)
        Naira = "N"
        amount = int(input("Enter amount.....:\n"))
        print('Your transaction was successful...')
        print('=' * 30)

        FoodBal = print('Your food budget balance is %s%d' % (Naira, amount))
        fff = amount

        cc = False
        while cc == False:
            choose = int(
                input("Enter to :: \n(1) Purchase food items \n(2) Withdraw \n(3) Compliant \n(4) exit \n"))
            if(choose == 1):
                cc = True
                print('Welcome to sea-shore food store;')
                print('We have all food items combined together to be a combo package,')

                summit = False
                while summit == False:

                    Jollof = print(
                        'The available combo packages are as follows::\n(1) Jollof rice combo package\n(2) Fried rice combo package\n(3) Egusi soup combo package')
                    fooditem = int(input('Select Input::\n'))
                    if (fooditem == 1):
                        summit = True
                        print("=" * 30)
                        ori = int(
                            input('For Jollof rice combo\n Enter to::\n(1) Proceed\n(2) Back\n'))

                        if (ori == 1):
                            ent = int(input(
                                'There are two quantity of jollof combo\nEnter::\n(1) small combo = N 5,000\n(2) Large Combo = N 10, 000 \n'))
                            if(ent == 1):
                                print(
                                    input("You are about to purchase, small combo!,\nenter \n(ok) to buy: "))
                                print('Your purchase was successful')
                                print('=' * 30)

                                N = 5000
                                B = fff - N
                                print("Your current balance is = %s%d " %
                                      (Naira, B))
                                Go = False
                                while Go == False:
                                    sss = int(
                                        input('Enter::\n(1) Back to the top page!, \n(2) Exit\n'))
                                    if(sss == 1):
                                        Go = True
                                        return ChooseOption().welcome()
                                    elif(sss == 2):
                                        Go = True
                                        exit()
                                    else:
                                        print('Invalid input')

                            elif(ent == 2):
                                print(
                                    input("You are about to purchase, Large combo!,\nenter \n(ok) to buy: "))
                                print('Your purchase was successful')
                                print('=' * 30)

                                N = 10000
                                B = fff - N
                                print("Your current balance is = %s%d" %
                                      (Naira, B))
                                Go = False
                                while Go == False:
                                    sss = int(
                                        input('Enter::\n(1) Back to the top page!, \n(2) Exit\n'))
                                    if(sss == 1):
                                        Go = True
                                        return ChooseOption().welcome()
                                    elif(sss == 2):
                                        Go = True
                                        exit()
                                    else:
                                        print('Invalid input')
                            else:
                                ('Invalid input! ')
                                summit = False

                        elif(ori == 2):
                            summit = False
                        else:
                            print('Invalid Input!')

                    elif(fooditem == 2):

                        print(
                            'This package is unavailable now, Choose another or try again later!')

                    elif(fooditem == 3):
                        print(
                            'This package is unavailable now, Choose another or try again later!')

                    else:
                        print('Invalid input, Choose an available option!')
            elif(choose == 2):
                cc = True
                print("Hey you just deposited! Do you want to Withdraw now?")
                pro = False
                while pro == False:
                    withdr = int(
                        input('Enter:: \n(1) Proceed  \n(2) complain \n(3) exit \n'))
                    if(withdr == 1):
                        pro = True
                        Continue = int(
                            input('How much do you want to withdraw?\n'))
                        print("=" * 30)
                        print('Your Transaction was successful')
                        print("=" * 30)
                        Naira = "N"
                        bal_wel = fff - Continue
                        new_bal = print('Your new balance is %s%d' %
                                        (Naira, bal_wel))
                        print('=' * 30)
                        now = datetime.datetime.now()
                        print('Current date and time:')
                        print(now.strftime("%Y-%m-%d %H:%M:%S"))
                        do = False
                        while do == False:
                            ent = int(
                                input('Enter:: \n(1) Complain\n(2) exit\n'))
                            if(ent == 1):
                                do = True
                                return Complaint().listen()
                            elif(ent == 2):
                                do = True
                                exit()
                            else:
                                print("Invalid input, Try again!")

                    elif(withdr == 2):
                        pro = True
                        return Complaint().listen()
                    elif(withdr == 3):
                        pro = True
                        exit()
                    else:
                        print('Invalid input, Try again')

            elif(choose == 3):
                cc = True
                return Complaint().listen()

            elif(choose == 4):
                cc = True
                now = datetime.datetime.now()
                print('Current date and time:')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                exit()

            else:
                print('Invalid Option, Try again')

    # def check_foodBal(food):

    #     now = datetime.datetime.now()
    #     print('Current date and time:')
    #     print(now.strftime("%Y-%m-%d %H:%M:%S"))
    #     return Budget().food.FoodBal

    @classmethod
    def cloths(cls):
        print('User you chose Clothing')
        print("=" * 30)
        Naira = "N"
        amount = int(input("Enter amount.....:\n"))
        print('Your transaction was successful...')
        print('=' * 30)

        ClothBal = print('Your cloth budget balance is %s%d' % (Naira, amount))
        fff = amount

        cc = False
        while cc == False:
            choose = int(
                input("Enter to :: \n(1) Purchase Cloths \n(2) Withdraw \n(3) Compliant \n(4) exit \n"))
            if(choose == 1):
                cc = True
                print('Welcome to sea-shore clothing store;')
                print(
                    'We have all cloths for (Male and female) combined together to be a combo package,')

                summit = False
                while summit == False:

                    Jollof = print(
                        'The available combo packages are as follows::\n(1) Jean, shirt and shoe combo \n(2) Male Undies [Boxers & singlets]\n(3) Female Undies [Pants & Bra] ')
                    fooditem = int(input('Select Input::\n'))
                    if (fooditem == 1):
                        summit = True
                        print("=" * 30)
                        ori = int(
                            input('For Jean, shirt and shoe combo\n Enter to::\n(1) Proceed\n(2) Back\n'))

                        if (ori == 1):
                            ent = int(input(
                                'There are two categorie of Jean, shirt and shoe combo\nEnter::\n(1) Male combo = N 25,000\n(2) Female Combo = N 30, 000 \n'))
                            if(ent == 1):
                                print(
                                    input("You are about to purchase, Male combo!,\nenter \n(ok) to buy: "))
                                print('Your purchase was successful')
                                print('=' * 30)

                                N = 25000
                                B = fff - N
                                print("Your current balance is = %s%d " %
                                      (Naira, B))
                                Go = False
                                while Go == False:
                                    sss = int(
                                        input('Enter::\n(1) Back to the top page!, \n(2) Exit\n'))
                                    if(sss == 1):
                                        Go = True
                                        return ChooseOption().welcome()
                                    elif(sss == 2):
                                        Go = True
                                        exit()
                                    else:
                                        print('Invalid input')

                            elif(ent == 2):
                                print(
                                    input("You are about to purchase, Female combo!,\nenter \n(ok) to buy: "))
                                print('Your purchase was successful')
                                print('=' * 30)

                                N = 30000
                                B = fff - N
                                print("Your current balance is = %s%d" %
                                      (Naira, B))
                                Go = False
                                while Go == False:
                                    sss = int(
                                        input('Enter::\n(1) Back to the top page!, \n(2) Exit\n'))
                                    if(sss == 1):
                                        Go = True
                                        return ChooseOption().welcome()
                                    elif(sss == 2):
                                        Go = True
                                        exit()
                                    else:
                                        print('Invalid input')
                            else:
                                ('Invalid input! ')
                                summit = False

                        elif(ori == 2):
                            summit = False
                        else:
                            print('Invalid Input!')

                    elif(fooditem == 2):

                        print(
                            'This package is unavailable now, Choose another or try again later!')

                    elif(fooditem == 3):
                        print(
                            'This package is unavailable now, Choose another or try again later!')

                    else:
                        print('Invalid input, Choose an available option!')
            elif(choose == 2):
                cc = True
                print("Hey you just deposited! Do you want to Withdraw now?")
                pro = False
                while pro == False:
                    withdr = int(
                        input('Enter:: \n(1) Proceed  \n(2) complain \n(3) exit \n'))
                    if(withdr == 1):
                        pro = True
                        Continue = int(
                            input('How much do you want to withdraw?\n'))
                        print("=" * 30)
                        print('Your Transaction was successful')
                        print("=" * 30)
                        Naira = "N"
                        bal_wel = fff - Continue
                        new_bal = print('Your new balance is %s%d' %
                                        (Naira, bal_wel))
                        print('=' * 30)
                        now = datetime.datetime.now()
                        print('Current date and time:')
                        print(now.strftime("%Y-%m-%d %H:%M:%S"))
                        do = False
                        while do == False:
                            ent = int(
                                input('Enter:: \n(1) Complain\n(2) exit\n'))
                            if(ent == 1):
                                do = True
                                return Complaint().listen()
                            elif(ent == 2):
                                do = True
                                exit()
                            else:
                                print("Invalid input, Try again!")

                    elif(withdr == 2):
                        pro = True
                        return Complaint().listen()
                    elif(withdr == 3):
                        pro = True
                        exit()
                    else:
                        print('Invalid input, Try again')

            elif(choose == 3):
                cc = True
                return Complaint().listen()

            elif(choose == 4):
                cc = True
                now = datetime.datetime.now()
                print('Current date and time:')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                exit()

            else:
                print('Invalid Option, Try again')

    def Entertain(cls):
        print('User you chose Entertainment')
        Naira = "N"
        amount = int(input("Enter amount.....:\n"))
        print('Your transaction was successful...')
        print('=' * 30)
        EnterBal = print('Your entertainment balance is %s%d' %
                         (Naira, amount))
        fff = amount

        cc = False
        while cc == False:
            choose = int(
                input("Enter to :: \n(1) Purchase Ticket For shows and games \n(2) Withdraw \n(3) Compliant \n(4) exit \n"))
            if(choose == 1):
                cc = True
                print('Welcome to sea-shore entertainment Center;')
                print('=' * 30)
                print(
                    'We have entertaining shows and games! ,')

                summit = False
                while summit == False:

                    Jollof = print(
                        'The available entertainment/show packages are as follows:\nBook your ticket::\n(1) Watch movies\n(2) Play Ps-5\n(3) Outdoor games ')
                    fooditem = int(input('Select Input::\n'))
                    if (fooditem == 1):
                        summit = True
                        print("=" * 30)
                        ori = int(
                            input('For latest movies and shows\n Enter to book ticket::\n(1) Proceed\n(2) Back\n'))

                        if (ori == 1):
                            ent = int(input(
                                'These are the available movies to watch\nEnter::\n(1) Coming To America 2 = N 5,000\n(2) Raya and the last dragon = N 3, 000 \n'))
                            if(ent == 1):
                                print(
                                    input("You are about to book a ticket to watch, Coming To America!,\nenter \n(ok) to buy: "))
                                print('Your purchase was successful')
                                print('=' * 30)

                                N = 5000
                                B = fff - N
                                print("Your current balance is = %s%d " %
                                      (Naira, B))
                                Go = False
                                while Go == False:
                                    sss = int(
                                        input('Enter::\n(1) Back to the top page!, \n(2) Exit\n'))
                                    if(sss == 1):
                                        Go = True
                                        return ChooseOption().welcome()
                                    elif(sss == 2):
                                        Go = True
                                        exit()
                                    else:
                                        print('Invalid input')

                            elif(ent == 2):
                                print(
                                    input("You are about to book a ticket to watch, Raya and the last dragon!,\nenter \n(ok) to buy: "))
                                print('Your purchase was successful')
                                print('=' * 30)

                                N = 3000
                                B = fff - N
                                print("Your current balance is = %s%d" %
                                      (Naira, B))
                                Go = False
                                while Go == False:
                                    sss = int(
                                        input('Enter::\n(1) Back to the top page!, \n(2) Exit\n'))
                                    if(sss == 1):
                                        Go = True
                                        return ChooseOption().welcome()
                                    elif(sss == 2):
                                        Go = True
                                        exit()
                                    else:
                                        print('Invalid input')
                            else:
                                ('Invalid input! ')
                                summit = False

                        elif(ori == 2):
                            summit = False
                        else:
                            print('Invalid Input!')

                    elif(fooditem == 2):

                        print(
                            'This package is unavailable now, Choose another or try again later!')

                    elif(fooditem == 3):
                        print(
                            'This package is unavailable now, Choose another or try again later!')

                    else:
                        print('Invalid input, Choose an available option!')
            elif(choose == 2):
                cc = True
                print("Hey you just deposited! Do you want to Withdraw now?")
                pro = False
                while pro == False:
                    withdr = int(
                        input('Enter:: \n(1) Proceed  \n(2) complain \n(3) exit \n'))
                    if(withdr == 1):
                        pro = True
                        Continue = int(
                            input('How much do you want to withdraw?\n'))
                        print("=" * 30)
                        print('Your Transaction was successful')
                        print("=" * 30)
                        Naira = "N"
                        bal_wel = fff - Continue
                        new_bal = print('Your new balance is %s%d' %
                                        (Naira, bal_wel))
                        print('=' * 30)
                        now = datetime.datetime.now()
                        print('Current date and time:')
                        print(now.strftime("%Y-%m-%d %H:%M:%S"))
                        do = False
                        while do == False:
                            ent = int(
                                input('Enter:: \n(1) Complain\n(2) exit\n'))
                            if(ent == 1):
                                do = True
                                return Complaint().listen()
                            elif(ent == 2):
                                do = True
                                exit()
                            else:
                                print("Invalid input, Try again!")

                    elif(withdr == 2):
                        pro = True
                        return Complaint().listen()
                    else:
                        print('Invalid input, Try again')
                pass
            elif(choose == 3):
                cc = True
                return Complaint().listen()

            elif(choose == 4):
                cc = True
                now = datetime.datetime.now()
                print('Current date and time:')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                exit()

            else:
                print('Invalid Option, Try again')

    def balancing(cls):                 # didnt used this also!!!!
        DataBase[FundsForFood] = []        # Didnt use this also!!!!


class Withdrawal:
    @staticmethod
    def with_confirm():
        print("Hey user, you can't withdraw yet!, Until you deposit first")
        print('=' * 30)
        check = False
        while check == False:
            ent = int(input('Deposit Now:\n(1) proceed \n(2) exit\n'))
            if(ent == 1):
                check = True
                return Depositing().Deposite()
            elif(ent == 2):
                check = True
                exit()
            else:
                print('Invalid input, Try again')


class Complaint:
    @staticmethod
    def listen():
        print(input("what are your complains???\n"))
        print("=" * 30)
        print('Thanks for contacting us..., We would see to your plight soon!')
        now = datetime.datetime.now()
        print('Current date and time:')
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        check = False
        while check == False:
            ent = int(input('Enter::\n(1) Back To the top page\n(2) exit\n'))
            if(ent == 1):
                check = True
                return ChooseOption().welcome()

            elif(ent == 2):
                check = True
                exit()
            else:
                print('Invalid input entered, Please Try again!')


class direct(Depositing, Withdrawal):  # trying to inherit from the listed classes
    @classmethod
    def direct_Selected(cls):

        selectopt = int(input(
            "Enter the respective input: \n(1) Deposit\n(2) Withdraw \n(3) Complaint\n"))
        if (selectopt == 1):
            return Depositing().Deposite()
        elif(selectopt == 2):
            return Withdrawal().with_confirm()
        elif(selectopt == 3):
            return Complaint().listen()
        else:
            print("Invalid input, Pls try again!")
            return direct().direct_Selected()


print(ChooseOption.welcome())


# Food_Deposit = FoodFundsOption()


# class FoodFundsOption:
#     def __init__(self, Deposit, Withdraw, Balance):
#         self.Deposit = Deposit
#         self.Withdraw = Withdraw
#         self.balance = Balance

#         select = int(
#             input('Select option \n(1) Deposit \n(2) Withdrawal \n(3) Check Balance \n'))
#         if (select == 1):
#             Naira = N
#             Depo = int(input("How much do you want to deposit"))
#             print('Your Transaction is being processed....')
#             print("=" * 5, +  "-" * 10, + "-" * 5)
#             print("Your balance is %d" % Depo)

#             Bal =

#         print("")

#         Deposit = int(input("How much do you want to deposit"))

#     def Check_FoodTotal(self):
#         return f"{select} "

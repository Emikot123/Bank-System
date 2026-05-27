class WrongChoice(Exception):
    pass

sign_history = {}


def sign_up(em, pa, na, ag, ba):

    if "@" in em and len(pa) > 8 and ag > 18 and ba > 0:
        sign_history[em] = pa
        user = User(em, pa, na, ag, ba, {}, {})
        main_menu()
    else:
        print("Wrong Email or Password or Too Broke or Young")
        sign()




def sign():
    print("1. Sign Up")
    print("2. Log In")
    print("3. Quit")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 0 or choice >= 3:
            raise WrongChoice
    except ValueError:
        print("Wrong Input")
        sign()
    except WrongChoice:
        print("Wrong Choice")
        sign()
    except:
        print("Try Again")
        sign()        

    else:
        if choice == 1:
            try:
                email67 = input("Enter your email: ")
                pass67 = input("Enter your password: ")
                name67 = input("Enter your name: ")
                age67 = int(input("Enter your age: "))
                balance67 = int(input("Enter your balance: "))
                if email67 in sign_history:
                    print("Email already used")
                    sign()
                else:
                    sign_up(email67,pass67,name67,age67,balance67)
            except ValueError:
                print("It should be a number!")
                sign()
            except:
                print("Smth went wrong")
                sign()
        
        elif choice == 2:
            while True:
                print("Enter your email and password(to quit type Q in one of them)")
                em45 = input("Enter email: ")
                pass45 = input("Enter password: ")
                if em45 in sign_history and sign_history[em45] == pass45:
                    main_menu()
                elif em45 == "Q" or pass45 == "Q":
                    sign()
                else:
                    print("Wrong")
                    continue
        elif choice == 3:
            print("Bye")


class User:

    def __init__(self, email, password, name, age, balance, history, loans):
        self.email = email
        self.password = password
        self.name = name
        self.age = age
        self.balance = balance
        self.history = history
        self.loans = loans
    
    def __ge__(self, value):
        return self.balance >= value
    
    def __str__(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Balance: {self.balance}")

    def deposit(self, money):
        self.balance += money
        self.history["Deposit"] = money
        print(f"Deposit. New Balance = {self.balance} Amount Added = {money}")

    def withdraw(self, money67):
        if self.balance >= money67:
            self.balance -= money67
            self.history["Withdraw"] = money67
            print(f"Withdraw. New Balance = {self.balance}. Amount = {money67}")


    def take_loan(self, item, cost):
        self.balance += cost
        self.loans[item] = cost
        print(f"Loan was taken. New Balance = {self.balance}. Cost = {cost}. Item = {item}")

def main_menu(): 
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Take a loan")
    print("4. Ongoing Loans")
    print("5. Profile")
    print("6. Quit")
    try:
        choice = int(input())
        if choice <= 0 or choice > 6:
            raise WrongChoice
    except WrongChoice:
        print("There is no such Choice")
        main_menu()    
    except:
        print("Wrong Input")
        main_menu()
    if choice == 1:
        try:
            amount67 = float(input("Enter amount to deposit: "))
            User.deposit(amount67)
            main_menu()

        except TypeError or ValueError:
            print("That is not a number!")
            main_menu()
        except:
            print("Wrong Input")
            main_menu()
    elif choice == 2:
        try:
            amount12 = float(input("Enter amount to withdraw: "))
            User.withdraw(amount12)
        except:
            print("Something went wrong. A cause may be wrong input.")

    elif choice == 3:
        item67 = input("Enter an item for loan taking: ")
        try:
            cost67 = float(input("Enter its cost: "))
        except:
            print("Wrong Input")
            main_menu()

        User.take_loan(item67, cost67)
        main_menu()

    elif choice == 4:

        for item12, value12 in loans:
            pass
    elif choice == 5:
        print(User)

    elif choice == 6:
        print("Bye")
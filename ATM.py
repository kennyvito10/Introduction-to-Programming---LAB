#Klementinus Kennyvito Salim - 2201811391
#ATM Program

class Account:                                                          #Make a class for Account
    def __init__(self,name,balance):                                    #Initiate a name and balance for an account
        self.n = str(name)
        self.b = float(balance)

    def getname(self):                                                  #Makes a function for calling the name
        return self.n

    def balance(self):                                                  #Makes a function for showing the balance
        return self.b

    def deposit(self,amount):                                           #Makes a function to deposit money to the account
        self.a = float(amount)
        self.b += self.a

    def withdraw(self,amount):                                          #Makes a function to withdraw money from the account
        if amount < self.b:                                             #Makes an if statement if to check whether the account has enough money to withdraw
            self.b -= amount

        else:                                                           #Prints a rejection message mentioning that you do not have enough balance
            print("Balance not enough. Go Earn Some Money!")

ATM = Account("Kenny",0)                                                #Calling the class Account
def main():                                                             #Makes the main function
    while True:                                                         #Loops the function
        print("Welcome To KKS ATM, {}!".format(ATM.getname()), "\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n5. Stop using ATM")
        usrInput = int(input("Enter Option: "))                                             #Prints the menu and asking user to input option

        if usrInput == 1:                                                                   #This will call out the deposit function and asking
            Amt = int(input("Enter Amount You Would like to Deposit:Rp. "))                 #the user the amount they want to deposit into the account
            print("Rp.", ATM.deposit(Amt))

        elif usrInput == 2:                                                                 #This will call out the withdraw function and asking
            Amt = int(input("Enter Amount You Would like to Withdraw:Rp. "))                #the user the amount they want to withdraw from the account
            print("Rp.",ATM.withdraw(Amt))

        elif usrInput == 3:                                                                 #This will call out the function to get the balance of the account
            print("Rp.",ATM.balance())

        elif usrInput == 4:                                                                 #This will end the program
            print("Thank You For Using This ATM! See you Next Time! ")
            quit()

print("Welcome to KKS ATM")                                                                 #Prints Bank Title

PIN = input("Enter Your PIN here: ")                                                        #inputting your pin

if PIN == "654321":                                                                         #If PIN is entered correctly, the program will execute
    main()

else:
    print("Sorry wrong PIN, ATM Cannot Connect")                                            #if PIN is entered incorrectly, the program will terminate
    quit()



#Klementinus Kennyvito Salim
#Quiz 02 Hotel Simulation Program
restart = "Y"

singleRooms = []                                                            #Making an empty lists of single and double rooms, and initiate grand Revenue to be 0

doubleRooms = []

grandRevenue = 0

class Hotel:                                                               #Making a Hotel class to define the customer name, get name, print room list, and the
    def __init__(self, name):                                              #Fees of the rooms
        self.name = str(name)

    def get_name(self):
        return self.name

    def roomlist(self):
        print("Single rooms : ",singleRooms)
        print("Double rooms : ",doubleRooms)

    def single_fee(self):
        return int(500000)

    def double_fee(self):
        return int(700000)

class CheckIn(Hotel):                                                     #Making a CheckIn class for defining check in functions for two categories of rooms
    def inSingle(self):
        if len(singleRooms) < 5:
            singleRooms.append(self.name)
            print("Have a Pleasant Stay, ", self.name, "!")
        else:
            print("Sorry, rooms are full right now. Please choose another category")
    def inDouble(self):
        if len(doubleRooms) < 5:
            doubleRooms.append(self.name)
            print("Have a Pleasant Stay, ", self.name, "!")
        else:
            print("Sorry, rooms are full right now. Please choose another category")
class CheckOut(Hotel):                                                    #Making a CheckOut class for defining check out functions for two categories of rooms
    def outSingle(self):
        return singleRooms.remove(self.name)

    def outDouble(self):
        return doubleRooms.remove(self.name)




def print_menu():                                       #Defining a funcition to print the menu
    print("="*29)
    print("Welcome to KKS Hotel! ")
    print("="*29)
    print("What do you want to do?")
    print("Pricing : Single : Rp. 500000")
    print("          Double : Rp. 700000")

def print_revenue():                                          #Defining a function to print total revenue
    print("-"*22)
    print("Total revenue: Rp. ",grandRevenue)
    print("-"*22)


runin = CheckIn                                         #operators for check in and check out class
runout = CheckOut

print_menu()

#starts the loop
while restart != ('N'):
    print("1. Check in \n2. Check out \n3. Check rooms list\n4. Revenue \n5. Quit")
    usrInput = input("Enter Option here: ")                                 #if user inputs 1, it carries out check in class
    if usrInput == "1":
        catInput = input("Single or Double? : ").lower()
        if catInput == "single":
            i = input("Enter Name : ")
            runin(i).inSingle()

        if catInput == "double":
            ii = input("Enter Name : ")
            runin(ii).inDouble()

    elif usrInput == "2":                                               #if user inputs 2, it carries out check out class
        o = input("Enter Room Type (Single/Double)").lower()
        if o == "single":
            oo = input("Enter Name here : ")
            runout(oo).outSingle()
            days = int(input("Enter number of days you stayed : "))
            grandRevenue += (runout(oo).single_fee()*days)
            print("Thank You for your time in here. We hope you enjoyed staying with us!")
            menu = input("Is there any other thing you want to do? (Y/N): ").lower()      #Asks if there is any other vehicles , else the program quits
            if menu == "n":
                quit()
        elif o == "double":
            op = input("Enter Name here : ")
            runout(op).outDouble()
            days = int(input("Enter number of days you stayed : "))
            grandRevenue += (runout(op).double_fee()*days)
            print("Thank You for your time in here. We hope you enjoyed staying with us!")
            menu = input("Is there any other thing you want to do? (Y/N): ").lower()      #Asks if there is any other vehicles , else the program quits
            if menu == "n":
                quit()
    elif usrInput == "3":                                               #if user input 3, it prints total room list
        Hotel("Ho").roomlist()
        menu = input("Is there any other thing you want to do? (Y/N): ").lower()      #Asks if there is any other vehicles , else the program quits
        if menu == "n":
           quit()
    elif usrInput == "4":                                               #if user inputs 4, it print the grand total revenue
        print_revenue()
        menu = input("Is there any other thing you want to do? (Y/N): ").lower()      #Asks if there is any other vehicles , else the program quits
        if menu == "n":
           quit()

    elif usrInput == "5":                                               #if user inputs 5, program will quit
        print("Thank You for using this System! \n See You!")
        quit()

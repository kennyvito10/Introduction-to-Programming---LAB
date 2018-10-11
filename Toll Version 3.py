#Klementinus Kennyvito Salim
#Toll Assignment Version 3
restart = "Y"                                                   #A variable to restart the program later on

Carlist1 = []                                                    #An empty list of Car, Bus, And Truck
Buslist1 = []
Trucklist1 = []
Carlist2 = []
Buslist2 = []
Trucklist2 = []


class Vehicle:                                                  #Making a Vehicle class which consists of three different types of vehicles: Car, Bus, Truck
    def __init__(self):
        self.fourwheels = "Car"
        self.sixwheels = "Bus"
        self.eightwheels = "Truck"

    def get_car(self):
        return self.fourwheels

    def get_bus(self):
        return self.sixwheels

    def get_truck(self):
        return self.eightwheels

class Vehicle2:                                                  #Making a Vehicle class which consists of three different types of vehicles: Car, Bus, Truck
    def __init__(self):
        self.fw = "Car"
        self.sw = "Bus"
        self.ew = "Truck"

    def get_car(self):
        return self.fw

    def get_bus(self):
        return self.sw

    def get_truck(self):
        return self.ew

class TollGate1(Vehicle):                                        #Making a TollGate class to define the Toll fees of the three different types of Vehicles,
                                                                #And also to add the vehicles to the list mentioned above
    def car_fee(self):
        return int(6000)

    def bus_fee(self):
        return int(8000)

    def truck_fee(self):
        return int(10000)

    def add_car(self):
        Carlist1.append(self.fourwheels)

    def add_bus(self):
        Buslist1.append(self.sixwheels)

    def add_truck(self):
        Trucklist1.append(self.eightwheels)

class TollGate2(Vehicle2):                                        #Making a TollGate class to define the Toll fees of the three different types of Vehicles,
                                                                #And also to add the vehicles to the list mentioned above
    def car_fee2(self):
        return int(18000)

    def bus_fee2(self):
        return int(20000)

    def truck_fee2(self):
        return int(25000)

    def add_car2(self):
        Carlist2.append(self.fw)

    def add_bus2(self):
        Buslist2.append(self.sw)

    def add_truck2(self):
        Trucklist2.append(self.ew)

class TollOperator1(TollGate1):                                  #Making a TollOperator Class to count the number of vehicles in each category,
                                                               #And to count the total revenue of the Toll fees from all the vehicles passing by
    def car_amt(self):
        return len(Carlist1)

    def bus_amt(self):
        return len(Buslist1)

    def truck_amt(self):
        return len(Trucklist1)

    def revenue(self):
        return ((self.car_amt() * self.car_fee()) +
                (self.bus_amt() * self.bus_fee()) +
                (self.truck_amt() * self.truck_fee()))

class TollOperator2(TollGate2):                                  #Making a TollOperator Class to count the number of vehicles in each category,
                                                               #And to count the total revenue of the Toll fees from all the vehicles passing by
    def car_amt2(self):
        return len(Carlist2)

    def bus_amt2(self):
        return len(Buslist2)

    def truck_amt2(self):
        return len(Trucklist2)

    def revenue(self):
        return ((self.car_amt2() * self.car_fee2()) +
                (self.bus_amt2() * self.bus_fee2()) +
                (self.truck_amt2() * self.truck_fee2()))

def print_menu1():                                             #Defining a function to print out the menu and header of the Toll Gate of Meruya
    print("="*75)
    print(" "*25, "Toll Payment Systems")
    print(" "*26, "PT Jasa Marga, Tbk.")
    print("="*75)
    print("Location of Toll Gate : Meruya")
    print("Category of vehicle: \n1. Car (RP 6000) \n2. Bus (RP 8000) \n3. Truck (RP 10000)\n")

def print_menu2():                                             #Defining a function to print out the menu of Pondok Aren
    print("Location of Toll Gate : Pondok Aren")
    print("Category of vehicle: \n1. Car (RP 18000) \n2. Bus (RP 20000) \n3. Truck (RP 25000)\n")

def print_revenue1():                                          #Defining a function to print out the amount of vehicles in each category
    print("\nLocation: Meruya")
    print("-"*22)                                             #And total revenue of vehicles
    print("Car     Bus     Truck")
    print("-"*22)
    print(operateToll.car_amt() ,"      ", operateToll.bus_amt(), "      ", operateToll.truck_amt())
    print("-"*22)
    print("Total revenue: Rp. ",operateToll.revenue())

def print_revenue2():                                          #Defining a function to print out the amount of vehicles in each category
    print("\nLocation: Pondok Aren")
    print("-"*22)                                             #And total revenue of vehicles
    print("Car     Bus     Truck")
    print("-"*22)
    print(operateToll_2.car_amt2() ,"      ", operateToll_2.bus_amt2(), "      ", operateToll_2.truck_amt2())
    print("-"*22)
    print("Total revenue: Rp. ",operateToll_2.revenue())
    print("\nGRAND TOTAL REVENUE: Rp. ",operateToll.revenue() + operateToll_2.revenue())
    print("\n\n<exit program>")



print_menu1()                                                  #Calls print_menu functions
print_menu2()

operateToll = TollOperator1()                                  #Operator for TollOperator Class
operateToll_2 = TollOperator2()

while restart != ('N'):                                       #Starts the loop
    inputloc = input("Enter Location of Tolls : Meruya / Pondok Aren?: ").lower()               #Asks the user to input location of toll gate
    if inputloc == "meruya":                                               #If input is Meruya, it will operate the operateToll operator and
        usrInput = input("Enter Vehicle Type: ").lower()
        if usrInput == "car":
            a = operateToll.get_car()
            b = operateToll.car_fee()
            z = operateToll.add_car()                                       #This adds 1 car to the Carlist1
            print(a, "Fee: ", b)
            menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program will print all revenue and quit
            if menu == "n":
                print_revenue1()
                print_revenue2()
                quit()

        if usrInput == "bus":                                             #If input is Bus, it will print out the Bus fee
            c = operateToll.get_bus()
            d = operateToll.bus_fee()
            y = operateToll.add_bus()                                      #This adds 1 bus to Buslist1
            print(c, "Fee: ", d)
            menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program will print revenue and quit
            if menu == "n":
                print_revenue1()
                print_revenue2()
                quit()

        if usrInput == "truck":                                           #If input is Truck, it will print out the Truck fee
            e = operateToll.get_truck()
            f = operateToll.truck_fee()
            x = operateToll.add_truck()                                     #This adds 1 truck to Trucklist1
            print(e, "Fee: ",f)
            menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program will print revenue and quit
            if menu == "n":
                print_revenue1()
                print_revenue2()
                quit()

    elif inputloc == "pondok aren":                                               #If location is Pondok Aren, it will operate operateToll_2 operator
        usrInput = input("Enter Vehicle Type: ").lower()
        if usrInput == "car":
            a = operateToll_2.get_car()
            b = operateToll_2.car_fee2()
            z = operateToll_2.add_car2()                                       #This adds 1 car to the Carlist2
            print(a, "Fee: ", b)
            menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program will print revenue and quit
            if menu == "n":
                print_revenue1()
                print_revenue2()
                quit()

        if usrInput == "bus":                                             #If input is Bus, it will print out the Bus fee
            c = operateToll_2.get_bus()
            d = operateToll_2.bus_fee2()
            y = operateToll_2.add_bus2()                                   #This adds 1 bus to Buslist2
            print(c, "Fee: ", d)
            menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program will print revenue and quit
            if menu == "n":
                print_revenue1()
                print_revenue2()
                quit()

        if usrInput == "truck":                                           #If input is Truck, it will print out the Truck fee
            e = operateToll_2.get_truck()
            f = operateToll_2.truck_fee2()
            x = operateToll_2.add_truck2()                              #This adds 1 bus to Trucklist2
            print(e, "Fee: ",f)
            menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program will print revenue and quit
            if menu == "n":
                print_revenue1()
                print_revenue2()
                quit()


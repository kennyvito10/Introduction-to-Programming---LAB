#Klementinus Kennyvito Salim
#Toll Assignment Version 2
restart = "Y"                                                   #A variable to restart the program later on

Carlist = []                                                    #An empty list of Car, Bus, And Truck
Buslist = []
Trucklist = []


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

class TollGate(Vehicle):                                        #Making a TollGate class to define the Toll fees of the three different types of Vehicles,
                                                                #And also to add the vehicles to the list mentioned above
    def car_fee(self):
        return int(6000)

    def bus_fee(self):
        return int(8000)

    def truck_fee(self):
        return int(10000)

    def add_car(self):
        Carlist.append(self.fourwheels)

    def add_bus(self):
        Buslist.append(self.sixwheels)

    def add_truck(self):
        Trucklist.append(self.eightwheels)
class TollOperator(TollGate):                                  #Making a TollOperator Class to count the number of vehicles in each category,
                                                               #And to count the total revenue of the Toll fees from all the vehicles passing by
    def car_amt(self):
        return len(Carlist)

    def bus_amt(self):
        return len(Buslist)

    def truck_amt(self):
        return len(Trucklist)

    def revenue(self):
        return ((self.car_amt() * self.car_fee()) +
                (self.bus_amt() * self.bus_fee()) +
                (self.truck_amt() * self.truck_fee()))

def print_menu():                                             #Defining a function to print out the menu and header of the Toll Gate
    print("="*75)
    print(" "*25, "Toll Payment Systems")
    print(" "*26, "PT Jasa Marga, Tbk.")
    print("="*75)
    print("Category of vehicle: \n1. Car (RP 6000) \n2. Bus (RP 8000) \n3. Truck (RP 10000)\n")

def print_revenue():                                          #Defining a function to print out the amount of vehicles in each category
    print("-"*22)                                             #And total revenue of vehicles
    print("Car     Bus     Truck")
    print("-"*22)
    print(operateToll.car_amt() ,"      ", operateToll.bus_amt(), "      ", operateToll.truck_amt())
    print("-"*22)
    print("Total revenue: Rp. ",operateToll.revenue())
    print("\n\n<exit program>")

print_menu()                                                  #Calls print_menu function

operateToll = TollOperator()                                  #Operator for TollOperator Class

while restart != ('N'):                                       #Starts the loop
    usrInput = input("Enter Vehicle Type here: ").lower()               #Asks the user to input the vehicle type
    if usrInput == "car":                                               #If input is Car, it will print out the Car fee
        a = operateToll.get_car()
        b = operateToll.car_fee()
        z = operateToll.add_car()                                       #This adds 1 car to the Carlist
        print(a, "Fee: ", b)
        menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program quits
        if menu == "n":
           print_revenue()
           quit()

    elif usrInput == "bus":                                             #If input is Bus, it will print out the Bus fee
        c = operateToll.get_bus()
        d = operateToll.bus_fee()
        y = operateToll.add_bus()
        print(c, "Fee: ", d)
        menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program quits
        if menu == "n":
           print_revenue()
           quit()

    elif usrInput == "truck":                                           #If input is Truck, it will print out the Truck fee
        e = operateToll.get_truck()
        f = operateToll.truck_fee()
        x = operateToll.add_truck()
        print(e, "Fee: ",f)
        menu = input("Is there any other vehicle (Y/N): ").lower()      #Asks if there is any other vehicles , else the program quits
        if menu == "n":
           print_revenue()
           quit()


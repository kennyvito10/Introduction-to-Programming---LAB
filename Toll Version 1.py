#Klementinus Kennyvito Salim
#Toll Assignment Version 1
restart = "Y"                       #A variable to restart the program later on

class Vehicle:                      #Making a Vehicle class which consists of three different types of vehicles: Car, Bus, Truck
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

class TollGate(Vehicle):           #Making a TollGate class to define the Toll fees of the three different types of Vehicles.

    def car_fee(self):
        return int(6000)

    def bus_fee(self):
        return int(8000)

    def truck_fee(self):
        return int(10000)


def print_menu():                  #Defining a function to print out the menu and header of the Toll Gate
    print("="*75)
    print(" "*25, "Toll Payment Systems")
    print(" "*26, "PT Jasa Marga, Tbk.")
    print("="*75)
    print("Category of vehicle: \n1. Car (RP 6000) \n2. Bus (RP 8000) \n3. Truck (RP 10000)\n")

print_menu()                       #Calls the print_menu function

operateToll = TollGate()           #Operator for TollGate Class

while restart != ('N'):            #Starting The loop
    usrInput = input("Enter Vehicle Type here: ").lower()                   #Asks the user to input the vehicle type
    if usrInput == "car":                                                   #If input is Car, it will print out the Car fee
        a = operateToll.get_car()
        b = operateToll.car_fee()
        print(a, "Fee: ", b)
        menu = input("Is there any other Vehicle (Y/N) ? : ").lower()       #Asks if there is any other vehicles , else the program quits
        if menu == "n":
            print("<exit program>")
            break

    elif usrInput == "bus":                                             #If input is Car, it will print out the Car fee
        c = operateToll.get_bus()
        d = operateToll.bus_fee()
        print(c, "Fee: ",d)
        menu = input("Is there any other Vehicle (Y/N) ? : ").lower()   #Asks if there is any other vehicles , else the program quits
        if menu == "n":
            print("<exit program>")
            break


    elif usrInput == "truck":                                           #If input is Car, it will print out the Car fee
        e = operateToll.get_truck()
        f = operateToll.truck_fee()
        print(e, "Fee: ",f)
        menu = input("Is there any other Vehicle (Y/N) ? : ").lower()   #Asks if there is any other vehicles , else the program quits
        if menu == "n":
            print("<exit program>")
            break




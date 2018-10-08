from datetime import datetime

class Cars:
    plate = ""

    def __init__(self, plate):
        self.plate = plate
        now = datetime.now().strftime("%H:%M")
        self.timein = datetime.strptime(now,"%H:%M")


    def getplate(self):
        return self.plate


class AllCars:
    listofcars = []

    def addcar(self,plate):
        self.listofcars.append(Cars(plate))

    def print_allcars(self):
        return self.listofcars

    def print_numcars(self):
        return len(self.listofcars)

    def calcprice(self,timeout):
        time_in = Cars(Cars.plate).timein
        time_out = datetime.strptime(timeout, "%H:%M")
        parktime = time_out - time_in
        timeParked = str(parktime).split(":")
        timeParkedhour = int(timeParked[0])
        if int(timeParked[1]) > 0:
            timeParkedhour += 1
        return timeParkedhour * 1000

    def removecars(self,car):
        if car in self.listofcars:
            self.listofcars.remove(car)


while True:
    print("1. Input License Plate \n2. Time Out and Price \n3. List of cars \n4. Remove Cars\n5. Quit")
    x = int(input("Option: "))

    if x == 1:
        usrInput = input("Plate: ")
        c = Cars(usrInput)
        timein = c.timein
        ca = AllCars()
        ca.addcar(c)
        print(c.getplate(),timein)
    elif x == 2:
        carprice = AllCars()
        timeoutinput = input("Enter time out at format: HH:MM : ")
        print("The price is Rp.{}".format(AllCars().calcprice(timeoutinput)))
    elif x == 3:
        j = AllCars().print_allcars()

    elif x == 4:
        inp = input("Enter the plate here: ")
        h = AllCars().removecars(inp)

    elif x == 5:
        print("Thank You!")
        quit()

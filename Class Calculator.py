class Calculator:                                      #Make a Class for calculator
    def __init__(self,n1,n2):                          #Initiate two variables to be inputted for calculation
        self.a = n1
        self.b = n2
    def add(self):                                     #Make a function of add for adding 2 numbers
        return self.a + self.b
    def min(self):                                     #Make a function of subtraction by subtracting second number from the first number
        return self.a - self.b
    def mul(self):                                     #Make a function of multiplication by multiplying the two numbers
        return self.a * self.b
    def div(self):                                     #Make a function of division by dividing second number from first number
        return self.a / self.b

satu = int(input("Enter first number: "))              #Assigning a variable so that it can input the first number
op = input("Enter Operator Here: ")                    #Assigning an input to input an operator
dua = int(input("Enter second number: "))              #Assinging a variable so that it can input the second number
oplist = ["+", "-", "*", "/"]                          #Make a list of operators

if op == oplist[0]:                                    #if function for Add module
    calc = Calculator(satu,dua)                        #Calls the function from input and exexuting the module from Calculator Class.
    print(calc.add())
if op == oplist[1]:                                    #if function for Subtraction module
    calc = Calculator(satu,dua)                        #Calls the function from input and exexuting the module from Calculator Class.
    print(calc.min())
if op == oplist[2]:                                    #if function for Multiplication module
    calc = Calculator(satu,dua)                        #Calls the function from input and exexuting the module from Calculator Class.
    print(calc.mul())
if op == oplist[3]:                                    #if function for Division module
    calc = Calculator(satu,dua)                        #Calls the function from input and exexuting the module from Calculator Class.
    print(calc.div())



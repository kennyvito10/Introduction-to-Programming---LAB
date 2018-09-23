num = int(input("Enter the number of rows you would like to create: "))

#First triangle
for row in range(0, num) :
    for column in range(0, row+1):
        print("*", end="")
    print("\n", end="")

#Second triangle
for row in range(0, num) :
    for column in range(0,num-row):
        print(" ", end="")

    for space in range(0,1+row):
        print("*", end="")
    print()

#Third triangle
for row in range(0, num) :
    for column in range(0,num-row):
        print("*", end="")

    for space in range(0,row-1):

        print(" ", end="")
    print()

#Fourth triangle
for row in range(0, num) :
    for column in range(0,row):
        print(" ", end="")

    for space in range(0,num-row):

        print("*", end="")
    print()

#Fifth pyramid
for row in range(0, num+1) :
    for column in range(0,num+1-row):
        print(" ", end="")

    for space in range(2,row*2+1):

        print("*", end="")

    print()
#sixth diamond
for row in range(0, num+1) :
    for column in range(0,(num+1)-row):
        print(" ", end="")

    for space in range(2,row*2+1):

        print("*", end="")
    print()
for row in range(0, num+1) :
    for column in range(0,row):
        print(" ", end="")

    for space in range(0,((num+1)-row)*2-1):

        print("*", end="")
    print()



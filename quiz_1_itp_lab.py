print("Refrigerator")

Refrigerator = True
location = ("""1. Top
    2. Middle
    3. Bottom""")

Top = {"Max":"15"}
Middle = {"Max":"15"}
Bottom = {"Mac":"15"}

items={"fish":"3",
       "water":"5"}

def put_top():
    for item in Top:
        if item not in Top:
            Top[item] = 1
        if item in Top :
            Top[item] +=1
def put_middle():
    for item in Middle:
        if item not in Middle:
            Middle[item] = 1
        if item in Middle:
            Middle[item] +=1
def put_bottom():
    for item in Bottom:
        if item not in Bottom:
            Bottom[item] = 1
        if item in Bottom:
            Bottom[item] +=1

def take_top():
    for item in Top:
        if item not in Top:
            Top[item] = 0
        if item in Top :
            Top[item] -=1
def take_middle():
    for item in Middle:
        if item not in Middle:
            Middle[item] = 0
        if item in Middle:
            Middle[item] -=1
def take_bottom():
    for item in Bottom:
        if item not in Bottom:
            Bottom[item] = 0
        if item in Bottom:
            Bottom[item] -=1


while Refrigerator:
    print("""1. Push
    2. Take""")

    user_input = input("Enter a number: ")

    print(user_input)

    if user_input == 1:
        print(location)
        inp = input("Where do you want to push/take: ")
        print(inp)
        if inp == 1:
            put_top()
        elif inp == 2:
            put_middle()
        elif inp == 3:
            put_bottom()
    if user_input == 2:
        print(location)
        inp = input("Where do you want to push/take:")
        print(inp)
        if inp == 1:
            take_top()
        elif inp == 2:
            take_middle()
        elif inp == 3:
            take_bottom()















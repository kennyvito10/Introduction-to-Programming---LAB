def a(q,w):
    ad = lambda o,p:o+p
    print(ad(q, w))
    return q,w
print(a(1,5))
add = lambda n1,n2:n1+n2

min = lambda n1,n2:n1-n2

mul = lambda n1,n2:n1*n2

div = lambda n1,n2:n1/n2

usrInput = input("Enter Numbers here: ")
usr = usrInput.split()
list = list(usr)
if list[1] == "+":
    print(add(int(list[0]),int(list[2])))
if list[1] == "-":
    print(min(int(list[0]),int(list[2])))
if list[1] == "*":
    print(mul(int(list[0]),int(list[2])))
if list[1] == "/":
    print(div(int(list[0]),int(list[2])))

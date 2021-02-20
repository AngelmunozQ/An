x = int(input("dame un numero : "))
y = int(input(" dame otro numero : "))
if x>=5:
    print (x,"mayor o igual que ",y)
elif x<=y:
    print(y,"mayor o igual que",x)
else:
    print("corrija")
    
# TAMBIEN CON FUNCIONES #
def mayoromenor (num1,num2):
    if num1>=num2:
        print("ok")
    elif num1<=num2:
        print("oo1")
    else:
        ("oki")
x=int(input("ingresa un numero: "))
y=int(input("ingresa otro numero :"))

mayoromenor(x,y)
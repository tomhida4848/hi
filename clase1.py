import random
a=input("nombre del jugador")
print(a)
b=input("nombre del jugador 2")
#print(b)
c=0
d=0
while c<=4 or d<=4:
    q=random.randint(0,1)
    if  q<=1:
        print(a)
        c+=1
    else:
        print(b)
        d+=1
        break
if c<=4:
    print("you win",a)
else:
    print("you win",b)
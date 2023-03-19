
c=True

while c==True:
    n=int(input("Ingresa un numero de 4 digitos: "))
    
    if(n>999 and n<10000):
        c=False
         

ninv=int(0)

while n!=0:
    mod=n%10
    ninv=ninv*10+(mod)
    n//=10

print("El número invertido es: ",ninv)
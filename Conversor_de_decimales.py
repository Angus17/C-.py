op=" "

while op!='d' and op!='D':#Prototipos de un Do{}While
    while True:
        op=str(input("Selecciona una opción: a.Decimal a binario | b.Decimal a octal | c.Decimal a Hexadecimal | d.Salir\n"))
        
        if(op=='a' or op=='b' or op=='c' or op=='d' or op=='A' or op=='B' or op=='C' or op=='D'):
           break
    if(op!='D' and op!='d'):
         n=int(input("Ingresa un numero a convertir: "))
         
    if(op=='A' or op=='a'):
        bin = " "
        while n!=0:
            a = n % 2
            n //= 2
            b = str(a)
            bin =str( b + bin )
        print("El numero en binario es de:", bin)
        
    elif(op=='B' or op=='b'):
        oct = " "
        while n!=0:
            a = n % 8
            n //= 8
            b = str(a)
            oct =str( b + oct )
        print("El numero en octal es de:", oct) 
        
    elif(op=='C' or op=='c'):
        HexD = " "
        while n!=0:
            a = n % 16
            n //= 16
            b = str(a)
            HexD =str( b + HexD )
        print("El numero en hexadecimal es de:", HexD)

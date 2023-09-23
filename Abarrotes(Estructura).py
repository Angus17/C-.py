def capturar_ventas():
    global lista
    lista = []
    i = 0
    j = 0
    subtotal = 0
    existencia_clientes = True
    
    while existencia_clientes:
        lista.append(dict())
        try:
            lista[i]["Folio"] = i + 1
            lista[i]["Articulos"] = []
            lista[i]["Articulos"].append(dict())
            existencia = True
            while existencia:
                lista[i]["Articulos"][j]["Nombre"] = input("Ingresa el nombre del articulo: ")
                while 1:
                    lista[i]["Articulos"][j]["Cantidad"] = int(input("Cuantos articulos compro: "))
                    if lista[i]["Articulos"][j]["Cantidad"] > 0:
                        break
                    else:
                        print("Ingresa datos correctos. . .")
                while 1:
                    lista[i]["Articulos"][j]["Precio_Unitario"] = float(input("Ingresa el precio por unidad: "))
                    if lista[i]["Articulos"][j]["Precio_Unitario"] > 0.0:
                        break
                    else:
                        print("Ingresa datos correctos. . .")
                subtotal += lista[i]["Articulos"][j]["Precio_Unitario"] * lista[i]["Articulos"][j]["Cantidad"] 
                while 1:
                    continuar = input("El cliente  compro mas poductos?\nEscribe:\nSi\nNo\n: ")
                    if continuar.lower() == "si":
                        os.system("pause")
                        os.system("cls")
                        lista[i]["Articulos"].append(dict())
                        j += 1 #Contador de productos
                        break
                    elif continuar.lower() == "no":
                        os.system("pause")
                        os.system("cls")
                        lista[i]["IVA"] = 0.16
                        lista[i]["Subtotal"] = subtotal
                        lista[i]["PRECIO_TOTAL (IVA incluido)"] = round(subtotal + (lista[i]["Subtotal"] * lista[i]["IVA"]), 2)
                        while 1:
                            existencia_clientes = input("Existen mas clientes?\nEscribe: Si/No\n: ")
                            if existencia_clientes.lower() == "si":
                                j = 0
                                subtotal = 0
                                i += 1 #Contador de clientes
                                break
                            elif existencia_clientes.lower() == "no":
                                existencia_clientes = False
                                break
                            else:
                                os.system("cls")
                                print("Favor de ingresar datos correctos. . .")
                                
                        existencia = False
                        break
                    else:
                        os.system("cls")
                        print("Ingresa una respuesta correcta. . .")
                        
        except ValueError:
            print("Debes ingresar un Valor adecuado")
        except TypeError:
            print("Debes ingresar un Tipo de dato correcto")
    os.system("pause")
    os.system("cls")
    return lista


def buscar_recibo_compras(lista_total):
    bandera = False
    
    while 1:
        try:
            buscar = int(input("Ingresa el numero de folio del recibo: "))
            for x in range(len(lista_total)):
                if buscar == lista_total[x]["Folio"]:
                    bandera = True
                    print("Recibo encontrado!. . .\n")
                    os.system("pause")
                    print(lista_total[x])
                    break
            if bandera:
                break
            else:
                print("No existe ningun recibo con el presente folio. . .")
        except ValueError:
            print("Ingresa un dato correcto por favor. . .")
        except TypeError:
            print("Verifica que los parametros sean compatibles. . .")
            exit()

def realizar_corte(lista_total):
    suma = 0
    print(f"Se recibio un total de {len(lista_total)} clientes!\n")
    for x in range(len(lista_total)):
        suma += lista_total[x]["PRECIO_TOTAL (IVA incluido)"]
    print(f"La tienda recaudo un total de ${suma} ")


def mostrar_historial(lista_total):
    for x in lista_total:
        print(f"{x}\n")



import os

lista = []

while 1:
    try:
        while 1:
            opcion = int(input("*****MENU DE ABARROTES*****\n1.Captuar ventas "
                            "\n2.Buscar recibo de compra\n3.Reailizar corte de caja\n"
                            "4.Mostrar historial de ventas\n5.Salir\nSelecciona una opcion: "))
            if 1 <= opcion <= 5:
                break
            else:
                print("Ingresa una opcion correcta. . .")
                os.system("pause")
                os.system("cls") 
        match opcion:
            case 1:
                os.system('cls')
                lista = capturar_ventas()
            case 2:
                if len(lista) != 0:
                    buscar_recibo_compras(lista)
                else:
                    os.system('cls')
                    print("Verifica la disponibilidad de clientes. . .")
                    os.system("pause")
                    
            case 3:
                if len(lista) != 0:
                    realizar_corte(lista)
                else:
                    os.system('cls')
                    print("Verifica la disponibilidad de clientes. . .")
                    os.system("pause")
                    
                
            case 4:
                if len(lista) != 0:
                    mostrar_historial(lista)
                else:
                    os.system('cls')
                    print("Verifica la disponibilidad de clientes. . .")
                    os.system("pause")
            case 5:
                break
    except ValueError:
        os.system("cls")
        print("Ingresa un dato valido y sin ausencia de valor. . .")
        os.system("pause")
        os.system("cls")
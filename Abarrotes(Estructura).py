def capturar_ventas(i):
    subtotal = 0
    j = 0
    existencia_clientes = True
    
    while existencia_clientes:
        try:
            lista.append(dict())
            lista[i]["Folio"] = i + 1
            lista[i]["Artículos"] = []
            lista[i]["Artículos"].append(dict())
            existencia = True
            while existencia:
                print(f"Cliente #{i + 1}", f"Producto {j + 1}\n", sep = "      ")
                lista[i]["Artículos"][j]["Nombre"] = input("Ingresa el nombre del artículo: ")
                while 1:
                    lista[i]["Artículos"][j]["Cantidad"] = int(input("Cuántos artículos compró: "))
                    if lista[i]["Artículos"][j]["Cantidad"] > 0:
                        break
                    else:
                        print("Ingresa datos correctos. . .")
                while 1:
                    lista[i]["Artículos"][j]["Precio_Unitario"] = float(input("Ingresa el precio por unidad: "))
                    if lista[i]["Artículos"][j]["Precio_Unitario"] > 0.0:
                        break
                    else:
                        print("Ingresa datos correctos. . .")
                subtotal += round((lista[i]["Artículos"][j]["Precio_Unitario"] * lista[i]["Artículos"][j]["Cantidad"]), 2)
                while 1:
                    continuar = input("El cliente  compró más poductos?\nEscribe: Si/No\n: ")
                    if continuar.lower() == "si":
                        os.system("pause")
                        os.system("cls")
                        lista[i]["Artículos"].append(dict())
                        j += 1 #Contador de productos
                        break
                    elif continuar.lower() == "no":
                        os.system("pause")
                        os.system("cls")
                        lista[i]["IVA"] = 0.16
                        lista[i]["Subtotal"] = round(subtotal,2)
                        lista[i]["PRECIO_TOTAL (IVA incluído)"] = round(subtotal + (lista[i]["Subtotal"] * lista[i]["IVA"]), 2)
                        while 1:
                            existencia_clientes = input("Existen mas clientes?\nEscribe: Si/No\n: ")
                            if existencia_clientes.lower() == "si":
                                os.system("pause")
                                os.system("cls")
                                j = 0
                                subtotal = 0
                                i += 1 #Contador de clientes nuevos
                                break
                            elif existencia_clientes.lower() == "no":
                                os.system("pause")
                                os.system("cls")
                                existencia_clientes = False
                                i += 1 #Se suma 1 cliente mas por si se selecciona de nuevo la funcion en el menu
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
            print("Debes ingresar un Valor adecuado. . .")
        except TypeError:
            print("Verifica que los parámetros sean compatibles. . .")
            exit()
    os.system("cls")
    return lista, i


def buscar_recibo_compras(lista_total):
    bandera = False
    
    while 1:
        try:
            buscar = int(input("Ingresa el número de folio del recibo: "))
            for x in range(len(lista_total)):
                if buscar == lista_total[x]["Folio"]:
                    bandera = True
                    os.system('cls')
                    print("Recibo encontrado!. . .\n")
                    print(lista_total[x])
                    os.system("pause")
                    os.system("cls")
                    break
            if bandera:
                break
            else:
                os.system("cls")
                print("No existe ningún recibo con el presente folio. . .")
                os.system("pause")
                os.system("cls")
                return
        except ValueError:
            print("Ingresa un dato correcto por favor. . .")
        except TypeError:
            print("Verifica que los parámetros sean compatibles. . .")
            exit()

def realizar_corte(lista_total):
    suma = 0
    print(f"¡Se recibió un total de {len(lista_total)} clientes!\n")
    for x in range(len(lista_total)):
        suma += lista_total[x]["PRECIO_TOTAL (IVA incluído)"]
    print(f"La tienda recaudó un total de ${round(suma,2)}\n")
    os.system("pause")
    os.system("cls")


def mostrar_historial(lista_total):
    for x in lista_total:
        print(f"{x}\n")
        
    os.system("pause")
    os.system("cls")



import os

lista = []
i = 0

while 1:
    try:
        while 1:
            opcion = int(input("*****MENÚ DE ABARROTES*****\n1.Captuar ventas "
                            "\n2.Buscar recibo de compra\n3.Realizar corte de caja\n"
                            "4.Mostrar historial de ventas\n5.Salir\nSelecciona una opción: "))
            if 1 <= opcion <= 5:
                break
            else:
                print("Ingresa una opción correcta. . .")
                os.system("pause")
                os.system("cls") 
        match opcion:
            case 1:
                os.system('cls')
                lista, i = capturar_ventas(i)
            case 2:
                if len(lista) != 0:
                    os.system('cls')
                    buscar_recibo_compras(lista)
                else:
                    os.system('cls')
                    print("Verifica la disponibilidad de clientes. . .")
                    os.system("pause")
                    os.system('cls')
            case 3:
                if len(lista) != 0:
                    os.system('cls')
                    realizar_corte(lista)
                else:
                    os.system('cls')
                    print("Verifica la disponibilidad de clientes. . .")
                    os.system("pause")
                    os.system('cls')
            case 4:
                if len(lista) != 0:
                    os.system('cls')
                    mostrar_historial(lista)
                else:
                    os.system('cls')
                    print("No se han recibido clientes aún. . .")
                    os.system("pause")
                    os.system('cls')
            case 5:
                os.system("cls")
                print("Finalizando programa. . .")
                break
    except ValueError:
        os.system("cls")
        print("Ingresa un dato válido y sin ausencia de valor. . .")
        os.system("pause")
        os.system("cls")
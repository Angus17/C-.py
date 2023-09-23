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
                        lista[i]["PRECIO_TOTAL (IVA incluido)"] = subtotal + (lista[i]["Subtotal"] * lista[i]["IVA"])
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
        print(lista)
        os.system("pause")
        os.system("cls")


def buscar_recibo_compras(Lista_total):
    while 1:
        buscar = int(input("Ingresa el numero de folio del recibo: "))
        for x in range(len(lista_total)):
            for y in lista_total.keys("Folio"):
                if buscar in lista_total[x][y]:
                    print(lista_total[x][y])
                    break
'''

def realizar_corte():

def mostrar_historial():
'''        



import os

lista_completa = []

while 1:
    while 1:
        
        opcion = int(input("*****MENU DE ABARROTES*****\n1.Captuar ventas "
                        "\n2.Buscar recibo de compra\n3.Reailizar corte de caja\n"
                        "4.Mostrar historial de ventas\n5.Salir\nSelecciona una opcion: "))
        if 1 <= opcion <= 5:
            break
        else:
            os.system("cls") 
    match opcion:
        case 1:
            capturar_ventas()
        case 2:
            if len(lista_completa) != 0:
                buscar_recibo_compras(lista)
            else:
                print("Verifica la disponibilidad de clientes. . .")
            '''
            case 3:
                
            case 4:
                
            '''
        case 5:
            break
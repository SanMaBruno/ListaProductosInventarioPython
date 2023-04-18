import os
opcion = True
tupla=("Nombre","Precio")
lista_productos=[]

def listar():
    print("\n\t\t\t Productos en inventario: \n")
    for key in lista_productos:
            print()
            print("\t\t\t------------------------------")
            print("\t\t\t",tupla[0],key[tupla[0]])
            print("\t\t\t",tupla[1],key[tupla[1]])
            print("\t\t\t------------------------------")

def insertar():
    while True:
        print("\t\t\t Agregar producto  \n""\t\t\t------------------------------")
        producto={}
        for i in range(0,len(tupla)):
            key=input(f"\t\t\t Ingrese {tupla[i]}: ")
            while key == "":
                print()
                print("\t\t\t ----------------------------------")
                print()
                print("\t\t\t Debe ingresar al menos un caracter.")
                print()
                print("\t\t\t ----------------------------------")
                print()
                key=input(f"\t\t\t ingrese {tupla[i]}: ")
            if (tupla[i]==tupla[1]):
                while not key.isdigit():
                    print()
                    print("\t\t\t ----------------------------------")
                    print()
                    print("\t\t\t Debes ingresar un valor numerico.")
                    print()
                    print("\t\t\t ----------------------------------")
                    print()
                    key=input(f"\t\t\t ingrese {tupla[i]}: ")
            producto[tupla[i]]=key
        lista_productos.append(producto)
        add=input("\t\t\t Presiona enter para agregar otro producto. De lo contrario escribe ""NO"" y presiona enter: ")
        if (add=='no' or add=='No' or add=='NO'or add=='nO'):
            break

def buscar(nombre):
    index = 0
    while index < len(lista_productos):
        if (nombre == lista_productos[index][tupla[0]]):
            return index
        index = index + 1
    return False

def modificar():
    while True:
        print("\n\t\t Registros: \n")
        listar()
        print("\n\t\t Modificar: \n")
        new_producto=input("\t\t\t Ingrese el producto a modificar: ")
        index = buscar(new_producto)
        if (not isinstance(index,bool)):
            modificar=input("\t\t\t Ingrese el nombre del nuevo producto: ")
            lista_productos[index][tupla[0]] =  modificar
            break
        else:
            print("\n\t\t\t El dato ingresado no existe el registro." )
            input("\t\t\t Presione enter para continuar...")
            os.system("clear")

def sumar():
    suma=0
    for key in lista_productos:
            suma=suma+int(key[tupla[1]])
    print("\t\t\t El valor total de los productos es $",suma)

def eliminar():
    print("\n\t\t Registros: \n")
    listar()
    eliminar=input("\t\t\t Ingrese el producto a eliminar: ")
    index = buscar(eliminar)
    if (not isinstance(index,bool)):
        lista_productos.pop(index)
    else:
        print("\t\t\t No existe el elemento a eliminar")

while opcion:
    os.system("clear")
    print()
    print("\t\t *** Programa de inventario ***\n")
    print ("\t\t\t ##### MENU ######")
    print ("\t\t\t------------------------")
    print()
    print ("\t\t\t a - Añadir un producto al inventario / Ver productos en inventario")
    print()
    print ("\t\t\t b - Salir")
    print()
    print ("\t\t\t------------------------")
    print()
    opcion_menu = input ("\t\t\t Selecciona una opcion:  ")

    if (opcion_menu == 'a'):
        flag_submenu = True
        while flag_submenu:
            os.system("cls")
            print ("\t\t\t##### SUBMENU ######")
            print ("\t\t\t------------------------")
            print()
            print ("\t\t\t 1 - Agregar un producto")
            print ("\t\t\t 2 - Productos ingresados")
            print ("\t\t\t 3 - Editar un producto ")
            print ("\t\t\t 4 - Valor total de todos los productos ingresados ")
            print ("\t\t\t 5 - Eliminar un producto")
            print ("\t\t\t 6 - Volver al menu principal")
            print()
            print ("\t\t\t------------------------")

            opcion_submenu = input("\t\t\t Ingrese una opcion submenu: ")
            if (opcion_submenu == '1'):
                print()
                insertar()
            elif (opcion_submenu == '2'):
                listar()
                input("\t\t\t Presione enter para continuar...")
            elif (opcion_submenu == '3'):
                modificar()
                input("\t\t\t Presione enter para continuar...")
            elif (opcion_submenu == '4'):
                sumar()
                input("\t\t\t Presione enter para continuar...")
            elif (opcion_submenu == '5'):
                eliminar()
                input("\t\t\t Presione enter para continuar...")
            elif (opcion_submenu == '6'):
                input("\t\t\t Has seleccionado volver. Presione enter para continuar...")
                flag_submenu = False
            else:
                print()
                print ("\t\t\t------------------------")
                input("\t\t\t OPCION INVALIDA. Presiona enter para continuar...")
                print ("\t\t\t------------------------")
                os.system("clear")

    elif (opcion_menu == 'b') :
        print("\t\t\t Has seleccionado Salir.")
        opcion = False
    else:
        print()
        print ("\t\t\t------------------------------------------------")
        input("\t\t\t Opcion no valida. Presione enter para continuar...")
        os.system("cls")

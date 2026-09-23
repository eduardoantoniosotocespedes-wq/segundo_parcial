lista = []

def agregar():
    print("ingrese 5 productos")
    for i in range(1,6):
        variable = str(input("por favor ingrese sus productos: "))
        lista.append(variable)
        i = i+1
    print(lista)

def alfavetico():
        lista.sort()
        print(lista)

def buscar():
     objeto = str(input("porfavor ingrese el nombre del producto que busca: "))
     if objeto in lista:
          print(f"su producto esta en la pocicion {lista(objeto)}")
     else:
          print("El producto no esta en la lista...")

while True:
     agregar()
     print("""MENU DE OPCIONES PARA USUSARIO
1.-Ver lista
2.-Solicitar un producto""")
     option = int(input("Responda aqui: "))
     match option:
          case 1:
               alfavetico() 
               break    
          case 2 :
               buscar()
               break
          case _:
               print("error....cerrado automatico")
               break  
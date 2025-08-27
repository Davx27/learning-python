#Fuctions Section
#One fuction
def addProduct():
    print("\nRegistre el producto ")
    nameProduct = input("Nombre del producto: ")
    productQuantity = int(input("Cantidad del producto: "))
    priceProduct = float(input("Precio del producto: "))
    print("Producto registrado con exito")
    
    products.append({"Nombre": nameProduct, "Cantidad": productQuantity, "Precio": priceProduct,})
    print(products)
    
#Second fuction
def showInventory():
    print("\n           ---Tu inventario---\n")
    if len(products) == 0:
        print("\n           Registra productos...")
    else:
        for product in products:
            print(f"Nombre: {product['Nombre']} | Canidad: {product['Cantidad']} | Precio: {product['Precio']}")
            
#Third fuction
def calculateTotalValue():
    print("\n           ---Precio total de todos los productos---")
    if len(products) == 0:
        print("\n           Refistra productos...")
    else:
        for product in products:
            total += product["Cantidad"] * product["Precio"]
            print(f"\n          El valor total del inventario es: {total}")
            


#Variable Section
products = []
#Variable boolean
menu = True


while menu:
    print("""
        _____________________________________________
        |                                           |
        |             Program Inventary             |
        |             ---BIENVENIDOS---             |
        |                                           |
        |-------------------------------------------|
        |                                           |
        |  1.Registrar producto                     |
        |  2.Mostrar Inventario                     |
        |  3.Calcular valor total                   |
        |  4.Buscar producto                        |
        |  5.Registrar venta                        |
        |  6.Salir del sistema                      |   
        |                                           |
        |___________________________________________|
        """)

    option = int(input("Seleccione una opcion: "))

    match option:
        case 1:
            print(addProduct())
        
        case 2:
            print(showInventory())
            
        case 3:
            print(calculateTotalValue())
            
    
    
    
            
            
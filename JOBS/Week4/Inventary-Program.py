#Fuctions Section
#One fuction
def addProduct():
    print("\nRegistre el producto ")
    nameProduct = input("Nombre del producto: ").lower()
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
            print(f"Nombre: {product['Nombre']} | Cantidad: {product['Cantidad']} | Precio: {product['Precio']}")
            
#Third fuction
def calculateTotalValue():
    print("\n           ---Precio total de todos los productos---")
    if len(products) == 0:
        print("\n           Refistra productos...")
    else:
        total = 0
        for product in products:
            total += product["Cantidad"] * product["Precio"]
        
        print(f"\n          El valor total del inventario es: {total}")
            

def findProduct():
    print("\n           ---Busca tu producto---")
    if len(products) == 0:
        print("\n           Registra productos...")
    else:
        productSelecUser = (input("\n            Escriba el producto que desea buscar: ")).lower()
        found = False 
        
        for product in products:
            if product['Nombre'].lower() == productSelecUser:
                print(f"\n          Nombre: {product['Nombre']} | Cantidad: {product['cantidad']} | Precio: {product['Precio']}")
                found = True 
                break
            
            else:
                print("\n           No se encuentra o digitelo tal cual lo registro...")    
            
            
            
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
        
        case 4:
            print(findProduct())
            
    
    
    
            
            
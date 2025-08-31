#Fuctions Section
#One fuction
def addProduct():
    add = True
    print("\nRegistre el producto ")
    while add:   
        nameProduct = input("Nombre del producto: ").lower()
        exists = False
        for product in products:
            if nameProduct == product['Nombre']:
                print("\n           No puedes agregar un producto con el mismo nombre de uno ya asignado")
                exists = True
        if exists:
            continue
            
        productQuantity = int(input("Cantidad del producto: "))
        priceProduct = float(input("Precio del producto: "))
        print("Producto registrado con exito")
            
        products.append({"Nombre": nameProduct, "Cantidad": productQuantity, "Precio": priceProduct, })
        print(products)
        add = False
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
        print("\n           Registra productos...")
    else:
        total = 0
        for product in products:
            total += product["Cantidad"] * product["Precio"]
        
        print(f"\n          El valor total del inventario es: {total}")
            
#Quarter fuction
def findProduct():
    find = True
    while find:
        print("\n           ---Busca tu producto---")
        if len(products) == 0:
            print("\n           Registra productos...")
        else:
            productSelecUser = (input("\n            Escriba el producto que desea buscar: ")).lower()
            found = False 
            
            for product in products:
                if product['Nombre'].lower() == productSelecUser:
                    print(f"\n          Nombre: {product['Nombre']} | Cantidad: {product['Cantidad']} | Precio: {product['Precio']}")
                    found = True 
                    find = False
                
            if not found:
                    print("\n           No se encuentra o digitelo tal cual lo registro...")    
            
#Fifth fuction
def saleRegistrer():
    print("\n           ---Busca tu producto---")
    if len(products) == 0:
        print("\n           Registra productos...")
    else:
        sale = True
        while sale:
            productSelecUser = (input("\n           Digite el producto que desea bsucar... :")).lower()
            found = False
            
            for product in products:
                if product['Nombre'].lower() == productSelecUser:
                    print(f"\n          Nombre: {product['Nombre']} | Cantidad: {product['Cantidad']} | Precio: {product['Precio']}")
                    found = True
                    productSold = int(input("\n            Ingrese la cantidad del producto vendido: "))
                    if productSold == 0:
                        print("\n           Registra la venta bien!!!")
                        
                    elif productSold <= product['Cantidad']:
                        product['Cantidad'] -= productSold 
                        print("\n           Venta del producto registrado con exito")
                        sale = False
                    else:
                        print("\n           No hay suficiente stock para esta venta")
                        
                    
            if not found:
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
            addProduct()
        
        case 2:
            showInventory()
        
        case 3:
            calculateTotalValue()
        
        case 4:
            findProduct()
            
        case 5:
            saleRegistrer()
            
        case 6:
            print("\n           Vuelva pronto...\n")
            menu = False 
    
    
    
            
            
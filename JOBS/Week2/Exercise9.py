#Login Sencillo: Crea un sistema de login simple que pida un nombre de usuario y una contraseña. Si coinciden

usuario_correcto = "David"
contrasena_correcta = "1234"

usuario = input("Ingresa tu nombre de usuario: ")
contrasena = input("Ingresa tu contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("¡Login exitoso! Bienvenido,", usuario)
else:
    print("Usuario o contraseña incorrectos.")

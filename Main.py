from Modulos.Menus import Menu_Inicial, MenuAdmin, MenuUser
from Modulos.Datos import*

JSON_UBICACION = "Datos/UsuariosServiciosProductos.json"

Datos = Cargar_datos(JSON_UBICACION)

print("*"*50)
print("")
print("BIENVENIDO".center(50))
print("")

Rol = Menu_Inicial(Datos)
if Rol == "Admin":
    MenuAdmin(Datos)
elif Rol == "User":
    MenuUser()
    
Guardar_datos(Datos, JSON_UBICACION)
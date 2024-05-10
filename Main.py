from Modulos.Menus import Menu_Inicial, MenuAdmin, MenuUser

print("*"*50)
print("")
print("BIENVENIDO".center(50))
print("")

Rol = Menu_Inicial()
print(Rol)
if Rol == "Admin":
    MenuAdmin()
elif Rol == "User":
    MenuUser()
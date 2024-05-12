import Modulos.GestionProductos
import Modulos.ManejoExcepiciones, Modulos.InicioSesion, Modulos.GestionUsuarios, Modulos.GestionServicios

UBI_DATOS = "Datos/UsuariosServiciosProductos.json"

def Menu_Inicial(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) SIGN IN".rjust(30))
        print("")
        print("")                               # Imprime las opciones del menu
        print("(2) SIGN UP".rjust(30))
        print("")
        print("")
        print("(3) SALIR".rjust(28))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Rol = Modulos.InicioSesion.SignIn()
            if  Rol == "Admin":
                return Rol
            elif Rol == "User":
                return Rol
            else:
                return 0
        elif choise == 2:
            print(2)
        elif choise == 3:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
        
def Eleccion_Numerica():
    try:
        choise = int(input("> "))
        return choise
    except ValueError:
        print("Valor Invalido")
        Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "42", "Menus.py")
    return(0)

def MenuAdmin(Datos):
    print("*"*50)
    print("")
    print("BIENVENIDO ADMIN".center(50))
    print("")
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Gestionar Usuarios".center(50))
        print("")
        print("")                               # Imprime las opciones del menu Admin
        print("(2) Gestionar Servicios".center(50))
        print("")
        print("")
        print("(3) Gestionar Productos".center(50))
        print("")
        print("")
        print("(4) Ver Reportes Comerciales".center(50))
        print("")
        print("")
        print("(5) Gestionar Ventas".center(50))
        print("")
        print("")
        print("(6) SALIR".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            MenuGestionarUsuarios(Datos)
        elif choise == 2:
            MenuGestionarServicios(Datos)
        elif choise == 3:
            MenuGestionarProductos(Datos)
        elif choise == 4:
            print(4)
        elif choise == 5:
            print(5)
        elif choise == 6:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuGestionarUsuarios(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Crear Perfiles de Usuarios".center(50))
        print("")
        print("")                                                        # Imprime las opciones del menu Gestionar Usuarios
        print("(2) Listar Perfiles de Usuarios".center(50))
        print("")
        print("")
        print("(3) Actualizar Perfil de Usuarios".center(50))
        print("")
        print("")
        print("(4) Eliminar Perfil de Usuarios".center(50))
        print("")
        print("")
        print("(5) VOLVER".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Datos = Modulos.GestionUsuarios.CrearPerfilesUsuarios(Datos)
        elif choise == 2:
            Modulos.GestionUsuarios.ListarPerfilesUsuarios(Datos)
        elif choise == 3:
            Datos = Modulos.GestionUsuarios.ActualizarPerfilesUsuarios(Datos)
        elif choise == 4:
            Datos = Modulos.GestionUsuarios.EliminarPerfilesUsuarios(Datos)
        elif choise == 5:
            print(5)
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
        
def MenuGestionarServicios(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Crear Servicios".center(50))
        print("")
        print("")                                                        # Imprime las opciones del menu Gestionar Usuarios
        print("(2) Listar Servicios".center(50))
        print("")
        print("")
        print("(3) Actualizar Servicios".center(50))
        print("")
        print("")
        print("(4) Eliminar Servicios".center(50))
        print("")
        print("")
        print("(5) VOLVER".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Datos = Modulos.GestionServicios.CrearServicios(Datos)
        elif choise == 2:
            Modulos.GestionServicios.ListarServicios(Datos)
        elif choise == 3:
            Datos = Modulos.GestionServicios.ActualizarServicios(Datos)
        elif choise == 4:
            Datos = Modulos.GestionServicios.EliminarServicios(Datos)
        elif choise == 5:
            print(5)
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuGestionarProductos(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Crear Productos".center(50))
        print("")
        print("")                                                        # Imprime las opciones del menu Gestionar Usuarios
        print("(2) Listar Productos".center(50))
        print("")
        print("")
        print("(3) Actualizar Productos".center(50))
        print("")
        print("")
        print("(4) Eliminar Productos".center(50))
        print("")
        print("")
        print("(5) VOLVER".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Datos = Modulos.GestionProductos.CrearProductos(Datos)
        elif choise == 2:
            Modulos.GestionProductos.ListarProductos(Datos)
        elif choise == 3:
            Datos = Modulos.GestionProductos.ActualizarProductos(Datos)
        elif choise == 4:
            Datos = Modulos.GestionProductos.EliminarProducto(Datos)
        elif choise == 5:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")

def MenuUser(Datos):
    print("Menu User")
"""    print("*"*50)
    print("")
    print("BIENVENIDO USER".center(50))
    print("")
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) SIGN IN".rjust(30))
        print("")
        print("")                               # Imprime las opciones del menu User
        print("(2) SIGN UP".rjust(30))
        print("")
        print("")
        print("(3) SALIR".rjust(28))
        print("")"""
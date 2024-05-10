import Modulos.ManejoExcepiciones
import Modulos.InicioSesion

def Menu_Inicial():
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
        elif choise == 2:
            print(2)
        elif choise == 3:
            print(3)
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
        
def Eleccion_Numerica():
    try:
        choise = int(input("> "))
        return(choise)
    except ValueError:
        print("Valor Invalido")
        Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "23", "Menus.py")
    return(0)

def MenuAdmin():
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
        print("(5) SALIR".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            MenuGestionarUsuarios()
        elif choise == 2:
            print(2)
        elif choise == 3:
            print(3)
        elif choise == 4:
            print(4)
        elif choise == 5:
            print(5)
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuGestionarUsuarios():
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
            print(1)
        elif choise == 2:
            print(2)
        elif choise == 3:
            print(3)
        elif choise == 4:
            print(4)
        elif choise == 5:
            print(5)
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
        
def MenuUser():
    print("*"*50)
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
        print("")
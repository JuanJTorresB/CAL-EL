import Modulos.ManejoExcepiciones
import Modulos.SignInSignUp

def Menu_Inicial():
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
        Modulos.SignInSignUp.SignIn()
    elif choise == 2:
        print(2)
    elif choise == 3:
        print(3)
    elif choise == 0:
        Menu_Inicial()
    else:
        print("Valor Invalido")
        Menu_Inicial()
    
def Eleccion_Numerica():
    try:
        choise = int(input("> "))
        return(choise)
    except ValueError:
        print("Valor Invalido")
        Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "23", "Menus.py")
    return(0)

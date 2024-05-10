import Modulos.ManejoExcepiciones

def PedirDocumento():
    try:
        Documento_Ingresado = int(input("Ingrese un Documento\n> "))
    except ValueError:
        Modulos.ManejoExcepiciones("Value Error", "7", "GestionUsuarios")
        PedirDocumento()
    else:
        if len(Documento_Ingresado) == 10:
            return Documento_Ingresado
        else:
            print("Longitud Invalida".center(50, "="))
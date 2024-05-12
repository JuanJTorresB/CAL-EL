import Modulos.ManejoExcepiciones
import Modulos.DatosYValidaciones
import Modulos.Menus

def CrearServicios(Datos):
    while True:
        Servicios = {}
        Servicios["Nombre_Servicio"] = str(input("Nombre del Servicio\n> "))
        Servicios["Codigo_Identificador"] = PedirCodigoIdentificador()
        Servicios["Tipo"] = Modulos.DatosYValidaciones.ValidacionTipoServicio()
        Servicios["Descripcion"] = str(input("Ingrese una descripcion de el Servicio\n> "))
        Servicios["Precio"] = Modulos.DatosYValidaciones.ValidacionPrecios("Precio")
        Servicios["Adquirido_por"] = []
        Datos["Servicios"].append(Servicios)
        return Datos
    
def ListarServicios(Datos):
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        print("Nombre del Servicio: ", Servicio["Nombre_Servicio"])
        print("Identificador: ", Servicio["Codigo_Identificador"])
        print("Tipo de Servicio: ", Servicio["Tipo"])
        print("Descripcion: ", Servicio["Descripcion"])
        print("Precio: ", Servicio["Precio"])
        print("")
        
def ActualizarServicios(Datos):
    Identidicador = PedirCodigoIdentificador()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            print("Que Desea Actualizar".center(50))
            print("(1) Nombre del Servicio".center(50))
            print("(2) Identificador".center(50))
            print("(3) Tipo".center(50))
            print("(4) Descripcion".center(50))
            print("(5) Precio".center(50))
            print("(0) Volver".center(50))
            while True:
                choise = Modulos.Menus.Eleccion_Numerica()
                if choise == 1:
                    Servicio["Nombre_Servicio"] = str(input("Nombre del Servicio\n> "))
                    return Datos
                elif choise == 2:
                    Identidicador_Validado = PedirCodigoIdentificador()
                    if IdentificadorNoRepetido(Identidicador_Validado, Datos):
                        print("Identidicador Repetido")
                        return Datos
                    else:
                        Servicio["Codigo_Identificador"] = Identidicador_Validado
                        return Datos
                elif choise == 3:
                    Servicio["Tipo"] = Modulos.DatosYValidaciones.ValidacionTipoServicio()
                    return Datos
                elif choise == 4:
                    Servicio["Descripcion"] = str(input("Ingrese una descripcion de el Servicio\n> "))
                    return Datos
                elif choise == 5:
                    Servicio["Precio"] = Modulos.DatosYValidaciones.ValidacionPrecios("Precio")
                    return Datos
                elif choise == 0:
                    print("")
                    return Datos
                else:
                    print("Valor Invalido")
                    return Datos
    print("Identidicador No Encontrado")
    return Datos
    
def EliminarServicios(Datos):
    Identidicador = PedirCodigoIdentificador()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            Servicios.remove(Servicio)
            Datos["Servicios"] = Servicios
            return Datos
    print("Identidicador No ENcontrado".center(50, "="))
    return Datos
    
def PedirCodigoIdentificador():
    while True:
            print("Introduce Un Codigo Identificador: ")
            Identidicador = Modulos.Menus.Eleccion_Numerica()
            if Identidicador != 0 and Identidicador > 0:
                break
            else:
                print("Debe ser un Numero, Diferente a 0 y Positivo")
    return Identidicador

def IdentificadorNoRepetido(Identificador, Datos):
    Servicios = Datos["Servicios"]
    for servicio in Servicios:
        if servicio["Codigo_Identificador"] == Identificador:
            return True
    return False

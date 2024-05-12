import Modulos.ManejoExcepiciones
import Modulos.DatosYValidaciones
import Modulos.Menus

def CrearServicios(Datos):
    while True:
        Servicios = {}
        Servicios["Nombre_Servicio"] = str(input("Nombre del Servicio\n> "))
        while True:
            print("Introduce Un Codigo Identificador: ")
            Identidicador = Modulos.Menus.Eleccion_Numerica()
            if Identidicador != 0 and Identidicador > 0:
                break
            else:
                print("Debe ser un Numero, Diferente a 0 y Positivo")
        Servicios["Codigo_Identificador"] = Identidicador
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
        print("Tipo de Servicio: ", Servicio["Tipo"])
        print("Descripcion: ", Servicio["Descripcion"])
        print("Precio: ", Servicio["Precio"])
        print("")
        
def ActualizarServicios(Datos):
    while True:
        print("Introduce Un Codigo Identificador: ")
        Identidicador = Modulos.Menus.Eleccion_Numerica()
        if Identidicador != 0 and Identidicador > 0:
            break
        else:
            print("Debe ser un Numero, Diferente a 0 y Positivo")
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            print("(1) Nombre del Servicio".center(50))
            print("(2) Tipo".center(50))
            print("(3) Descripcion".center(50))
            print("(4) Precio".center(50))
            while True:
                choise = Modulos.Menus.Eleccion_Numerica()
                if choise == 1:
                    Servicio["Nombre_Servicio"] = str(input("Nombre del Servicio\n> "))
                    return Datos
                elif choise == 2:
                    Documento_Validado = Modulos.DatosYValidaciones.PedirDocumento()
                    if Modulos.DatosYValidaciones.DocumentoNoRepetido(Documento_Validado, Datos):
                        print("Documento Repetido")
                        return Datos
                    else:
                        user["Documento"] = Documento_Validado
                elif choise == 3:
                    user["Rol"] = Modulos.DatosYValidaciones.Validacion_Rol()
                    return Datos
                elif choise == 4:
                    user["Fecha_Nacimiento"] = Modulos.DatosYValidaciones.ValidacionFechaNacimiento()
                    return Datos
                elif choise == 0:
                    print("Valor Invalido")
                    return Datos
                else:
                    print("Valor Invalido")
                    return Datos
    print("Documento No Encontrado")
    
def EliminarPerfilesUsuarios(Datos):
    Documento_Usuario = Modulos.DatosYValidaciones.PedirDocumento()
    Usuarios = Datos["Usuarios"]
    for user in Usuarios:
        if user["Documento"] == Documento_Usuario:
            Usuarios.remove(user)
            Datos["Usuarios"] = Usuarios
            return Datos
    print("Documento No ENcontrado".center(50, "="))
    

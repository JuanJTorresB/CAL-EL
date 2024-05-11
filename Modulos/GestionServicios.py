import Modulos.ManejoExcepiciones
import Modulos.DatosYValidaciones
import Modulos.Menus

def CrearServicios(Datos):
    while True:
        Producto = {}
        Producto["Nombre_Servicio"] = str(input("Nombre del Servicio\n> "))
        Producto["Tipo"] = "Prepago"
        Producto["Descripcion"] = str(input("Ingrese una descripcion de el Servicio"))
        Producto["Precio"] = Modulos.DatosYValidaciones.ValidacionPrecios("Precio")
        Datos["Productos"].append(Producto)
        return Datos
    
def ListarPerfilesUsuarios(Datos):
    Usuarios = Datos["Usuarios"]
    for Usuario in Usuarios:
        print(Usuario)
        print("")
        
def ActualizarPerfilesUsuarios(Datos):
    Documento_Usuario = Modulos.DatosYValidaciones.PedirDocumento()
    Usuarios = Datos["Usuarios"]
    for user in Usuarios:
        if user["Documento"] == Documento_Usuario:
            print("(1) Nombre_User".center(50))
            print("(2) Documento".center(50))
            print("(3) Rol".center(50))
            print("(4) Fecha_Nacimiento".center(50))
            print("(5) Genero".center(50))
            print("(6) Ciudad".center(50))
            print("(7) Direccion_User".center(50))
            print("(8) Telefono_Celular".center(50))
            print("(9) Correo_Electronico".center(50))
            print("(10) Categoria".center(50))
            print("(0) Volver".center(50))
            choise = Modulos.Menus.Eleccion_Numerica()
            if choise == 1:
                user["Nombre_User"] = str(input("Nombre del User\n> "))
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
            elif choise == 5:
                user["Genero"] = Modulos.DatosYValidaciones.ValidacionGenero()
                return Datos
            elif choise == 6:
                user["Ciudad"] = Modulos.DatosYValidaciones.ValidacionNoVacioLetras("Ingrese su Ciudad de Residencia\n")
                return Datos
            elif choise == 7:
                user["Informacion_de_Contacto"]["Direccion_User"] = Modulos.DatosYValidaciones.ValidacionNoVacioAceptaEspacios(input("Direccion de Residencia\n> "))
                return Datos
            elif choise == 8:
                user["Informacion_de_Contacto"]["Telefono_Celular"] = Modulos.DatosYValidaciones.ValidacionNumeroCelular()
                return Datos
            elif choise == 9:
                user["Informacion_de_Contacto"]["Correo_Electronico"] = Modulos.DatosYValidaciones.ValidacionNoVacioAceptaEspacios(input("Correo Electronico\n> "))
                return Datos
            elif choise == 10:
                user["Historial"]["Categoria"] = Modulos.DatosYValidaciones.ValidacionCategoriaCliente()
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
    

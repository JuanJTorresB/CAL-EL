import Modulos.ManejoExcepiciones
import Modulos.DatosYValidaciones
import Modulos.Menus

def CrearPerfilesUsuarios(Datos):
    while True:
        Usuario = {}
        Informacion_de_Contacto = {}
        Historial = {}
        Usuario["Nombre_User"] = str(input("Nombre del User\n> "))
        Documento_Validado = Modulos.DatosYValidaciones.PedirDocumento()
        if Modulos.DatosYValidaciones.DocumentoNoRepetido(Documento_Validado, Datos):
            print("Documento Repetido")
            break
        Usuario["Documento"] = Documento_Validado
        Usuario["Rol"] = Modulos.DatosYValidaciones.Validacion_Rol()
        Usuario["Fecha_Nacimiento"] = Modulos.DatosYValidaciones.ValidacionFechaNacimiento()
        Usuario["Genero"] = Modulos.DatosYValidaciones.ValidacionGenero()
        Usuario["Ciudad"] = Modulos.DatosYValidaciones.ValidacionNoVacioLetras("Ingrese su Ciudad de Residencia\n")
        Informacion_de_Contacto["Direccion_User"] = Modulos.DatosYValidaciones.ValidacionNoVacioAceptaEspacios(input("Direccion de Residencia\n> "))
        Informacion_de_Contacto["Telefono_Celular"] = Modulos.DatosYValidaciones.ValidacionNumeroCelular()
        Informacion_de_Contacto["Correo_Electronico"] = Modulos.DatosYValidaciones.ValidacionNoVacioAceptaEspacios(input("Correo Electronico\n> "))
        Historial["Categoria"] = Modulos.DatosYValidaciones.ValidacionCategoriaCliente()
        Historial["Reclamaciones"] = []
        Historial["Sugerencias"] = []
        Usuario["Informacion_de_Contacto"] = Informacion_de_Contacto
        Usuario["Historial"] = Historial
        Datos["Usuarios"].append(Usuario)
        return Datos
    
def ListarPerfilesUsuarios(Datos):
    Usuarios = Datos["Usuarios"]
    for Usuario in Usuarios:
        print("Nombre: ", {Usuario["Nombre_User"]})
        print("Documento:", {Usuario["Documento"]})
        print("Rol:", {Usuario["Rol"]})
        print("Fecha de Nacimiento: ", {Usuario["Fecha_Nacimiento"]})
        print("Genero: ", {Usuario["Genero"]})
        print("Ciudad: ", {Usuario["Ciudad"]})
        print("Informacion de Contacto")
        print(Usuario["Informacion_de_Contacto"]["Direccion_User"].center(50))
        print(Usuario["Informacion_de_Contacto"]["Telefono_Celular"].center(50))
        print(Usuario["Informacion_de_Contacto"]["Correo_Electronico"].center(50))
        print("Historial")
        print(Usuario["Historial"]["Categoria"].center(50))
        print("Reclamaciones".center(50))
        Reclamaciones = Usuario["Historial"]["Reclamaciones"]
        for reclamacion in Reclamaciones:
            print(reclamacion["Fecha"].center(50))
            print(reclamacion["Descripcion"].center(50))
        print("Sugerencias".center(50))
        Sugerencias = Usuario["Historial"]["Sugerencias"]
        for Sugerencia in Sugerencias:
            print(Sugerencia["Fecha"].center(50))
            print(Sugerencia["Descripcion"].center(50))
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
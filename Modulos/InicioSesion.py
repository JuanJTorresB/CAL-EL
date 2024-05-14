from Modulos.DatosYValidaciones import PedirDocumento, DocumentoNoRepetido, ValidacionFechaNacimiento, ValidacionGenero, ValidacionNoVacioLetras, ValidacionNoVacioAceptaEspacios, ValidacionNumeroCelular
import Modulos.Menus
import json

JSON_UBICACION = "Datos/UsuariosServiciosProductos.json"
USUARIO_ACTUAL_UBUCACION = "Datos/UsuarioActual.txt"

def SignIn(Datos):
    Documento_Ingresado = PedirDocumento()
    Usuarios = Datos["Usuarios"]
    for user in Usuarios:
        if user["Documento"] == Documento_Ingresado and user["Rol"] == "Admin":
            with open(USUARIO_ACTUAL_UBUCACION,"w") as file:
                file.write(Documento_Ingresado)
            return "Admin"
        elif user["Documento"] == Documento_Ingresado and user["Rol"] == "User":
            with open(USUARIO_ACTUAL_UBUCACION,"w") as file:
                file.write(Documento_Ingresado)
            return "User"
    print("Documento No Encontrado".center(50, "="))
    return 0

def SignUp(Datos):
    Usuario = {}
    Informacion_de_Contacto = {}
    Historial = {}
    print("Permitanos La Siguiente Informacion Para Registrarlo")
    Usuario["Nombre_User"] = str(input("Nombre\n> "))
    while True:
        Documento_Validado = PedirDocumento()
        if DocumentoNoRepetido(Documento_Validado, Datos):
            print("Documento Repetido")
        else:
            break
    Usuario["Documento"] = Documento_Validado
    Usuario["Rol"] = "User"
    Usuario["Fecha_Nacimiento"] = ValidacionFechaNacimiento()
    Usuario["Genero"] = ValidacionGenero()
    Usuario["Ciudad"] = ValidacionNoVacioLetras("Ingrese su Ciudad de Residencia\n")
    Informacion_de_Contacto["Direccion_User"] = Modulos.DatosYValidaciones.ValidacionNoVacioAceptaEspacios(input("Ingrese su Direccion de Residencia\n> "))
    Informacion_de_Contacto["Telefono_Celular"] = Modulos.DatosYValidaciones.ValidacionNumeroCelular()
    Informacion_de_Contacto["Correo_Electronico"] = Modulos.DatosYValidaciones.ValidacionNoVacioAceptaEspacios(input("Ingrese su Correo Electronico\n> "))
    Historial["Categoria"] = "Nuevo Cliente"
    Historial["Reclamaciones"] = []
    Historial["Sugerencias"] = []
    Usuario["Informacion_de_Contacto"] = Informacion_de_Contacto
    Usuario["Historial"] = Historial
    Datos["Usuarios"].append(Usuario)
    with open(USUARIO_ACTUAL_UBUCACION,"w") as file:
        file.write(Documento_Validado)
    print("Perfil Creado Con Exito")
    return Datos
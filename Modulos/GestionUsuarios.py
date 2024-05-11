import Modulos.ManejoExcepiciones
import Modulos.DatosYValidaciones


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
        print(Usuario)
        print("")
        
def ActualizarPerfilesUsuarios(Datos):
    a = 5
    return Datos

def EliminarPerfilesUsuarios(Datos):
    Documento_Usuario = Modulos.DatosYValidaciones.PedirDocumento()
    Usuarios = Datos["Usuarios"]
    for user in Usuarios:
        if user["Documento"] == Documento_Usuario:
            Datos["Usuarios"] = Usuarios.pop(user)
            return Datos
    print("Documento No ENcontrado".center("=", 50))

    """     "Nombre_User" : "Daniela Andrea Lizarazo Lamus",
            "Documento" : "1097494374",
            "Rol" : "Admin",
            "Fecha_Nacimiento" : "2006/02/6",
            "Genero" : "F",
            "Ciudad" : "Bucaramanga",
            "Informacion_de_Contacto" : 
            {
                "Direccion_User" : "Calle 204A #40-194",
                "Telefono_Celular" : "3204828077",
                "Correo_Electronico" : "Dani@gmail.com"
            },
            "Historial" :
            {
                "Categoria" : "Cliente Leal",
                "Reclamaciones" : [""],
                "Sugerencias" : [""]
            }"""
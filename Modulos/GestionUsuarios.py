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
        Usuario["Genero"] = "F"
        Usuario["Ciudad"] = "Bucaramanga"
        Informacion_de_Contacto["Direccion_User"] = "Calle 204A #40-194"
        Informacion_de_Contacto["Telefono_Celular"] = "3204828077"
        Informacion_de_Contacto["Correo_Electronico"] = "Dani@gmail.com"
        Historial["Categoria"] = "Cliente Leal"
        Historial["Reclamaciones"] = []
        Historial["Sugerencias"] = []
        Usuario["Informacion_de_Contacto"] = Informacion_de_Contacto
        Usuario["Historial"] = Historial
        Datos["Usuarios"].append(Usuario)
        return Datos
    
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
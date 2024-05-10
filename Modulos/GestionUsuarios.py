import Modulos.ManejoExcepiciones

def PedirDocumento():
    while True:
        try:
            Documento_Ingresado = int(input("Ingrese un Documento\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "7", "GestionUsuarios")
        else:
            Documento_Ingresado = str(Documento_Ingresado)
            if len(Documento_Ingresado) == 10:
                return Documento_Ingresado
            else:
                print("Longitud Invalida".center(50, "="))

def CrearPerfilesUsuarios(Datos):
    Usuario = {}
    Informacion_de_Contacto = {}
    Historial = {}
    Usuario["Nombre_User"] = "A"
    Usuario["Documento"] = PedirDocumento()
    Usuario["Rol"] = "Admin"
    Usuario["Fecha_Nacimiento"] = "2006/02/6"
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
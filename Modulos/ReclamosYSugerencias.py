from datetime import date

UBI_USUARIO_ACTUAL = "Datos/UsuarioActual.txt"

def RegistrarReclamos(Datos):
    Usuarios = Datos["Usuarios"]
    with open(UBI_USUARIO_ACTUAL, "r") as Cedula_User_file:
        Cedula_User = Cedula_User_file.read()
    for Usuario in Usuarios:
        if int(Usuario["Documento"]) == int(Cedula_User):
            print("Dinos tu Reclamo")
            Reclamo = str(input("> "))
            Reclamaciones = Usuario["Historial"]["Reclamaciones"]
            Reclamacion = {}
            Reclamacion["Fecha"] = str(date.today())
            Reclamacion["Descripcion"] = Reclamo
            Reclamaciones.append(Reclamacion)
            print("Reclamo Guardado, Soporte Tecnico se pondra en Contacto Contigo :3")
            return Datos
    print("No estas Registrado")
    return Datos
    
def RegistrarSugerencias(Datos):
    Usuarios = Datos["Usuarios"]
    with open(UBI_USUARIO_ACTUAL, "r") as Cedula_User_file:
        Cedula_User = Cedula_User_file.read()
    for Usuario in Usuarios:
        if int(Usuario["Documento"]) == int(Cedula_User):
            print("Dinos tu Sugerencia")
            Sugerencia_Input = str(input("> "))
            Sugerencias = Usuario["Historial"]["Sugerencias"]
            Sugerencia = {}
            Sugerencia["Fecha"] = str(date.today())
            Sugerencia["Descripcion"] = Sugerencia_Input
            Sugerencias.append(Sugerencia)
            print("Sugerencia Guardada, Muchas Gracias :3")
            return Datos
    print("No estas Registrado")
    return Datos
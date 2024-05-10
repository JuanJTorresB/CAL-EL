from Modulos.DatosYValidaciones import PedirDocumento
import Modulos.Menus
import json

JSON_UBICACION = "Datos/UsuariosServiciosProductos.json"
USUARIO_ACTUAL_UBUCACION = "Datos/UsuarioActual.txt"

def SignIn():
    Documento_Ingresado = PedirDocumento()
    file = open(JSON_UBICACION)
    file_antes_mod = json.load(file)
    Usuarios = file_antes_mod["Usuarios"]
    for user in Usuarios:
        if user["Documento"] == Documento_Ingresado and user["Rol"] == "Admin":
            return "Admin"
        elif user["Documento"] == Documento_Ingresado and user["Rol"] == "User":
            with open(USUARIO_ACTUAL_UBUCACION,"w") as file:
                file.write(Documento_Ingresado)
            return "User"
    print("")
    print("Documento No Encontrado".center(50, "="))
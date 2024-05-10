import json
import Modulos.ManejoExcepiciones

def Cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos
        
        

def Guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    
def Validacion_Rol():
    while True:
        try:
            Rol_Ingresado = int(input('Ingrese el Rol del Perfil (1) "Admin" (2) "User"\n> '))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "25", "DatosYValidaciones")
        else:
            if Rol_Ingresado == 1:
                return("Admin")
            elif Rol_Ingresado == 2:
                return("User")
            else:
                print("Opcion No valida".center(50, "="))
                
def DocumentoNoRepetido(Documento, Datos):
    Usuarios = Datos["Usuarios"]
    for user in Usuarios:
        if user["Documento"] == Documento:
            return True
    return False

def PedirDocumento():
    while True:
        try:
            Documento_Ingresado = int(input("Ingrese un Documento\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "46", "DatosYValidaciones")
        else:
            Documento_Ingresado = str(Documento_Ingresado)
            if len(Documento_Ingresado) == 10:
                return Documento_Ingresado
            else:
                print("Longitud Invalida".center(50, "="))
                
def ValidacionAnio():
    while True:
        try:
            ValidacionAño = int(input("Año en el formato AAAA\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "59", "DatosYValidaciones")
            print("Año Invalido".center(50, "="))
        else:
            ValidacionAño_Str = str(ValidacionAño)
            if len(ValidacionAño_Str) == 4:
                return ValidacionAño

def ValidacionMes():
    while True:
        try:
            ValidacionMes = int(input("Més en el formato MM\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "71", "DatosYValidaciones")
            print("Més Invalido".center(50, "="))
        else:
            ValidacionMes_Str = str(ValidacionMes)
            if len(ValidacionMes_Str) == 2:
                return ValidacionMes
            
def ValidacionDia():
    while True:
        try:
            ValidacionDia = int(input("Més en el formato DD\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "71", "DatosYValidaciones")
            print("Dia Invalido".center(50, "="))
        else:
            ValidacionDia_Str = str(ValidacionDia)
            if len(ValidacionDia_Str) == 2:
                return ValidacionDia
            
    
                
def ValidacionFechaNacimiento():
    print("Escribe la Fecha de Nacimiento en el formato AAAA/MM/DD")
    Anio = ValidacionAnio()
    Mes = ValidacionMes()
    Dia = ValidacionDia()
    return(f"{Anio}/{Mes}/{Dia}")
    
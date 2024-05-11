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
            ValidacionAnio = int(input("Año en el formato AAAA\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "59", "DatosYValidaciones")
            print("Año Invalido".center(50, "="))
        else:
            ValidacionAnio_Str = str(ValidacionAnio)
            if len(ValidacionAnio_Str) == 4 and ValidacionAnio< 2024:
                return ValidacionAnio

def ValidacionMes():
    while True:
        try:
            ValidacionMes = int(input("Més en el formato MM\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "71", "DatosYValidaciones")
            print("Més Invalido".center(50, "="))
        else:
            ValidacionMes_Str = str(ValidacionMes)
            if len(ValidacionMes_Str) <= 2 and ValidacionMes <= 12 and ValidacionMes > 0:
                return ValidacionMes
            
def ValidacionDia():
    while True:
        try:
            ValidacionDia = int(input("Dia en el formato DD\n> "))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "71", "DatosYValidaciones")
            print("Dia Invalido".center(50, "="))
        else:
            ValidacionDia_Str = str(ValidacionDia)
            if len(ValidacionDia_Str) <= 2 and ValidacionDia <= 31 and ValidacionDia > 0:
                return ValidacionDia
                
def ValidacionFechaNacimiento():
    print("Escribe la Fecha de Nacimiento en el formato AAAA/MM/DD")
    Anio = ValidacionAnio()
    Mes = ValidacionMes()
    Dia = ValidacionDia()
    return(f"{Anio}/{Mes}/{Dia}")
    
def ValidacionGenero():
    while True:
        try:
            Rol_Ingresado = int(input('Ingrese el Genero para el Perfil (1) "F" (2) "M" (3) "Otro"\n> '))
        except ValueError:
            Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "25", "DatosYValidaciones")
        else:
            if Rol_Ingresado == 1:
                return("F")
            elif Rol_Ingresado == 2:
                return("M")
            elif Rol_Ingresado == 3:
                return("Otro")
            else:
                print("Opcion No valida".center(50, "="))

def ValidacionNoVacioLetras(Input_Generico):
    print("SIN ESPACIOS")
    while True:
        if bool(Input_Generico):
            return Input_Generico
        elif not Input_Generico.isalpha():
            print("Valor Invalido".center(50, "="))
            Input_Generico = input("> ")
        else:
            print("Valor Invalido".center(50, "="))
            Input_Generico = input("> ")
            
def ValidacionNoVacioNumeros(Input_Generico):
    print("SIN ESPACIOS")
    while True:
        if bool(Input_Generico):
            return Input_Generico
        elif not Input_Generico.isalnum():
            print("Valor Invalido".center(50, "="))
            Input_Generico = input("> ")
        else:
            print("Valor Invalido".center(50, "="))
            Input_Generico = input("> ")
            
def ValidacionNoVacioAceptaEspacios(Input_Generico):
    while True:
        if bool(Input_Generico):
            return Input_Generico
        else:
            print("Valor Invalido".center(50, "="))
            Input_Generico = input("> ")
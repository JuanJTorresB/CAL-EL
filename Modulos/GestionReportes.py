from Modulos.GestionVentas import PedirCodigoIdentificador
from Modulos.DatosYValidaciones import ValidacionNoVacioLetras

def ContarCantidadVendidasProducto(Datos):
    print("Ingrese el Codigo Para Ver La Cantidad Vendida del Producto")
    Contador = 0
    Identidicador = PedirCodigoIdentificador()
    Productos = Datos["Productos"]
    for Produto in Productos:
        if Produto["Codigo_Identificador"] == Identidicador:
            for Adquisiciones in Produto["Adquirido_por"]:
                Contador += Adquisiciones["Cantidad"]
    print("Se Han Vendido: ", Contador)
    
def ContarCantidadVendidasServicio(Datos):
    print("Ingrese el Codigo Para Ver La Cantidad Vendida del Servicio")
    Contador = 0
    Identidicador = PedirCodigoIdentificador()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            for Adquisiciones in Servicio["Adquirido_por"]:
                Contador += Adquisiciones["Cantidad"]
    print("Se Han Vendido: ", Contador)
    
def ContarProductosPorCiudad(Datos):
    print("Ingrese el Codigo Para Ver La Cantidad Vendida del Producto por Ciudad")
    Contador = 0
    Ciudades = []
    Identidicador = PedirCodigoIdentificador()
    Productos = Datos["Productos"]
    for Produto in Productos:
        if Produto["Codigo_Identificador"] == Identidicador:
            for Adquisiciones in Produto["Adquirido_por"]:
                Ciudades.append(Adquisiciones["Ciudad"])
    Ciudades = set(Ciudades)
    Ciudades = list(Ciudades)
    print("¿De estas Ciudades?")
    print(Ciudades)
    Ciudad_Input = ValidacionNoVacioLetras("¿Cual desea Conocer la cantidad de Ventas?")
    if Ciudad_Input in Ciudades:
        for Produto in Productos:
            if Produto["Codigo_Identificador"] == Identidicador:
                for Adquisiciones in Produto["Adquirido_por"]:
                    if Adquisiciones["Ciudad"] == Ciudad_Input:
                        Contador += Adquisiciones["Cantidad"]
        print("Se Han Vendido: ", Contador)
    else:
        print('En "{Ciudad_Input}" No Han habido Ventas de este Producto')

def ContarServiciosPorCiudad(Datos):
    print("Ingrese el Codigo Para Ver La Cantidad Vendida del Servicio por Ciudad")
    Contador = 0
    Ciudades = []
    Identidicador = PedirCodigoIdentificador()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            for Adquisiciones in Servicio["Adquirido_por"]:
                Ciudades.append(Adquisiciones["Ciudad"])
    Ciudades = set(Ciudades)
    Ciudades = list(Ciudades)
    print("¿De estas Ciudades?")
    print(Ciudades)
    Ciudad_Input = ValidacionNoVacioLetras("¿Cual desea Conocer la cantidad de Ventas?")
    if Ciudad_Input in Ciudades:
        for Servicio in Servicios:
            if Servicio["Codigo_Identificador"] == Identidicador:
                for Adquisiciones in Servicio["Adquirido_por"]:
                    if Adquisiciones["Ciudad"] == Ciudad_Input:
                        Contador += Adquisiciones["Cantidad"]
        print("Se Han Vendido: ", Contador)
    else:
        print('En "{Ciudad_Input}" No Han habido Ventas de este Servicio')
        
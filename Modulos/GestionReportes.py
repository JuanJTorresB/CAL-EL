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
    
def ContarPorCiudad(Datos):
    print("Ingrese La ciudad")
    Ciudad = ValidacionNoVacioLetras()
    Contador = 0
    Identidicador = PedirCodigoIdentificador()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            for Adquisiciones in Servicio["Adquirido_por"]:
                Contador += Adquisiciones["Cantidad"]
    print("Se Han Vendido: ", Contador)
from Modulos.GestionProductos import PedirCodigoIdentificador
from Modulos.DatosYValidaciones import PedirDocumento, DocumentoNoRepetido, ValidacionTipodeVentadeProductos
from Modulos.Menus import Eleccion_Numerica
from datetime import date
def RegistrarVentaProductos(Datos):
    print("Para Encontra El Producto")
    Identidicador = PedirCodigoIdentificador()
    Productos = Datos["Productos"]
    for Producto in Productos:
        if Producto["Codigo_Identificador"] == Identidicador:
            Facturas = Producto["Adquirido_por"]
            Factura = {}
            Documento_Validado = PedirDocumento()
            if not DocumentoNoRepetido(Documento_Validado, Datos):
                print("Documento de Usuario No Registrado")
                return Datos
            Factura["Documento"] = Documento_Validado
            Factura["Fecha_Adquisicion"] = date.today()
            Factura["Estado"] = ValidacionTipodeVentadeProductos()
            Factura["Cantidad"] = Eleccion_Numerica() 
            Facturas.append(Factura)
            Producto["Adquirido_por"] = Facturas
            Datos["Productos"] = Productos
            return Datos
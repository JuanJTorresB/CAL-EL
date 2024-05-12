from Modulos.GestionProductos import PedirCodigoIdentificador
from Modulos.DatosYValidaciones import PedirDocumento, DocumentoNoRepetido, ValidacionTipodeVentadeProductos
import Modulos.Menus
from datetime import date

def RegistrarVentaProductos(Datos):
    print("Para Encontra El Producto")
    Identidicador = PedirCodigoIdentificador()
    Productos = Datos["Productos"]
    for Producto in Productos:
        if Producto["Codigo_Identificador"] == Identidicador:
            Factura = {}
            Documento_Validado = PedirDocumento()
            if not DocumentoNoRepetido(Documento_Validado, Datos):
                print("Documento de Usuario No Registrado")
                return Datos
            Factura["Documento"] = Documento_Validado
            Factura["Fecha_Adquisicion"] = "2024/12/05"
            Factura["Estado"] = ValidacionTipodeVentadeProductos()
            print("Cantidad")
            Factura["Cantidad"] = Modulos.Menus.Eleccion_Numerica()
            Producto["Adquirido_por"].append(Factura)
            return Datos
    return Datos
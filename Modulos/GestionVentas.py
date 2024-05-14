from Modulos.GestionProductos import PedirCodigoIdentificador
from Modulos.DatosYValidaciones import PedirDocumento, DocumentoNoRepetido, ValidacionTipodeVentadeProductos, ValidacionTipoServicio, ValidacionTipodeVentadeServicios, ValidacionNoVacioLetras
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
            Factura["Ciudad"] = ValidacionNoVacioLetras("Ingrese la Ciudad en la que se Realizo la Venta")
            Factura["Fecha_Adquisicion"] = str(date.today())
            Factura["Estado"] = ValidacionTipodeVentadeProductos()
            print("Cantidad")
            Factura["Cantidad"] = Modulos.Menus.Eleccion_Numerica()
            Producto["Adquirido_por"].append(Factura)
            return Datos
    print("Producto No Encontrado")
    return Datos

def RegistrarVentaServicios(Datos):
    print("Para Encontra El Servicio")
    Identidicador = PedirCodigoIdentificador()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            Factura = {}
            Documento_Validado = PedirDocumento()
            if not DocumentoNoRepetido(Documento_Validado, Datos):
                print("Documento de Usuario No Registrado")
                return Datos
            Factura["Documento"] = Documento_Validado
            Factura["Ciudad"] = ValidacionNoVacioLetras("Ingrese la Ciudad en la que se Realizo la Venta")
            Factura["Fecha_Adquisicion"] = str(date.today())
            Factura["Estado"] = ValidacionTipodeVentadeServicios()
            print("Cantidad")
            Factura["Cantidad"] = Modulos.Menus.Eleccion_Numerica()
            Servicio["Adquirido_por"].append(Factura)
            return Datos
    print("Servicio No Encontrado")
    return Datos

def ListarVentasServicios(Datos):
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        print("Nombre del Servicio: ", Servicio["Nombre_Servicio"])
        print("Identificador: ", Servicio["Codigo_Identificador"])
        print("Tipo de Servicio: ", Servicio["Tipo"])
        print("Descripcion: ", Servicio["Descripcion"])
        print("Precio: ", Servicio["Precio"])
        print("")
        print("Compras Registradas:")
        for Registro in Servicio["Adquirido_por"]:
            print("")
            print("Documento: ", Registro["Documento"])
            print("Ciudad de Adquisicion: ", Registro["Ciudad"])
            print("Fecha_Adquisicion: ", Registro["Fecha_Adquisicion"])
            print("Estado: ", Registro["Estado"])
            print("Cantidad: ", Registro["Cantidad"])
            print("")

def ListarVentasProductos(Datos):
    Productos = Datos["Productos"]
    for Producto in Productos:
        print("Nombre del Producto: ", Producto["Nombre_Producto"])
        print("Identificador: ", Producto["Codigo_Identificador"])
        print("Tipo de Producto: ", Producto["Tipo"])
        print("Descripcion: ", Producto["Descripcion"])
        print("Precio: ", Producto["Precio"])
        for Registro in Producto["Adquirido_por"]:
            print("Documento: ", Registro["Documento"])
            print("Ciudad de Adquisicion: ", Registro["Ciudad"])
            print("Fecha_Adquisicion: ", Registro["Fecha_Adquisicion"])
            print("Estado: ", Registro["Estado"])
            print("Cantidad: ", Registro["Cantidad"])
            print("")
            
def ActualizarVentasServicios(Datos):
    print("Para Encontra El Servicio")
    Identidicador = PedirCodigoIdentificador()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Codigo_Identificador"] == Identidicador:
            for Adquisiciones in Servicio["Adquirido_por"]:
                Documento_Validado = PedirDocumento()
                if int(Adquisiciones["Documento"]) == int(Documento_Validado):
                    print("Que desea Actualizar".center(50))
                    print("(1) Estado")
                    print("(2) Cantidad")
                    print("(3) Ciudad de la Venta")
                    choise = Modulos.Menus.Eleccion_Numerica()
                    if choise == 1:
                        Adquisiciones["Estado"] = ValidacionTipodeVentadeServicios()
                        return Datos
                    elif choise == 2:
                        print("Cantidad")
                        Adquisiciones["Cantidad"] = Modulos.Menus.Eleccion_Numerica()
                        return Datos
                    elif choise == 3:
                        Adquisiciones["Ciudad"] = ValidacionNoVacioLetras("Ingrese la Ciudad en la que se Realizo la Venta")
                        return Datos
                    elif choise == 0:
                        print("")
                        return Datos
                    return Datos
            print("Documento No Registrado En este Servicio, No ha comprado es Servicio")
            return Datos
    print("Servicio No Encontrado")
    return Datos

def ActualizarVentasProductos(Datos):
    print("Para Encontra El Produto")
    Identidicador = PedirCodigoIdentificador()
    Productos = Datos["Productos"]
    for Produto in Productos:
        if Produto["Codigo_Identificador"] == Identidicador:
            for Adquisiciones in Produto["Adquirido_por"]:
                Documento_Validado = PedirDocumento()
                if int(Adquisiciones["Documento"]) == int(Documento_Validado):
                    print("Que desea Actualizar".center(50))
                    print("(1) Estado")
                    print("(2) Cantidad")
                    print("(3) Ciudad de la Venta")
                    choise = Modulos.Menus.Eleccion_Numerica()
                    if choise == 1:
                        Adquisiciones["Estado"] = ValidacionTipodeVentadeProductos()
                        return Datos
                    elif choise == 2:
                        print("Cantidad")
                        Adquisiciones["Cantidad"] = Modulos.Menus.Eleccion_Numerica()
                        return Datos
                    elif choise == 3:
                        Adquisiciones["Ciudad"] = ValidacionNoVacioLetras("Ingrese la Ciudad en la que se Realizo la Venta")
                        return Datos
                    elif choise == 0:
                        print("")
                        return Datos
                    return Datos
            print("Documento No Registrado En este Producto, No ha comprado es Producto")
            return Datos
    print("Producto No Encontrado")
    return Datos
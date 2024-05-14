from Modulos.DatosYValidaciones import ValidacionTipoServicio, ValidacionTipodeProducto

def CatalogoServicios(Datos):
    Tipo_Ingresado = ValidacionTipoServicio()
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        if Servicio["Tipo"] == Tipo_Ingresado:
            print("")
            print("Nombre del Servicio: ", Servicio["Nombre_Servicio"])
            print("Tipo de Servicio: ", Servicio["Tipo"])
            print("Descripcion: ", Servicio["Descripcion"])
            print("Precio: ", Servicio["Precio"])
            print("")
            
def CatalogoProductos(Datos):
    Tipo_Ingresado = ValidacionTipodeProducto()
    Productos = Datos["Productos"]
    for Producto in Productos:
        if Producto["Tipo"] == Tipo_Ingresado:
            print("Nombre del Producto: ", Producto["Nombre_Producto"])
            print("Tipo de Producto: ", Producto["Tipo"])
            print("Descripcion: ", Producto["Descripcion"])
            print("Marca: ", Producto["Marca"])
            print("Precio: ", Producto["Precio"])
            print("")
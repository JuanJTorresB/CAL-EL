from Modulos.DatosYValidaciones import ValidacionTipoServicio, ValidacionTipodeProducto

UBI_USUARIO_ACTUAL = "Datos/UsuarioActual.txt"

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

def ProductoMasPopularPaisUser(Datos):
    Ciudades = []
    Productos = Datos["Productos"]
    for Produto in Productos:
        for Adquisiciones in Produto["Adquirido_por"]:
            Ciudades.append(Adquisiciones["Ciudad"])
    Ciudades = set(Ciudades)
    Ciudades = list(Ciudades)
    Usuarios = Datos["Usuarios"]
    with open(UBI_USUARIO_ACTUAL, "r") as Cedula_User_file:
        Cedula_User = Cedula_User_file.read()
    for Usuario in Usuarios:
        if int(Usuario["Documento"]) == int(Cedula_User):
            Ciudad_User =  Usuario["Ciudad"]
    Mayor = 0
    Contador = 0
    Mayor = 0
    if Ciudad_User in Ciudades:
        for Produto in Productos:
            for Adquisiciones in Produto["Adquirido_por"]:
                if Adquisiciones["Ciudad"] == Ciudad_User:
                    Contador += Adquisiciones["Cantidad"]
            if Contador > Mayor:
                NombreProducto = Produto["Nombre_Producto"]
            Contador = 0
    else:
        Productos = Datos["Productos"]
        for Produto in Productos:
            for Adquisiciones in Produto["Adquirido_por"]:
                Contador += Adquisiciones["Cantidad"]
            if Contador > Mayor:
                Mayor = Contador
                NombreProducto = Produto["Nombre_Producto"]
            Contador = 0
    print(f'Te recomendamos el Producto "{NombreProducto}"')

def ServicioMasPopularPaisUser(Datos):
    Ciudades = []
    Servicios = Datos["Servicios"]
    for Servicio in Servicios:
        for Adquisiciones in Servicio["Adquirido_por"]:
            Ciudades.append(Adquisiciones["Ciudad"])
    Ciudades = set(Ciudades)
    Ciudades = list(Ciudades)
    Usuarios = Datos["Usuarios"]
    with open(UBI_USUARIO_ACTUAL, "r") as Cedula_User_file:
        Cedula_User = Cedula_User_file.read()
    for Usuario in Usuarios:
        if int(Usuario["Documento"]) == int(Cedula_User):
            Ciudad_User =  Usuario["Ciudad"]
    Mayor = 0
    Contador = 0
    Mayor = 0
    if Ciudad_User in Ciudades:
        for Servicio in Servicios:
            for Adquisiciones in Servicio["Adquirido_por"]:
                if Adquisiciones["Ciudad"] == Ciudad_User:
                    Contador += Adquisiciones["Cantidad"]
            if Contador > Mayor:
                NombreServicio = Servicio["Nombre_Servicio"]
            Contador = 0
    else:
        Servicios = Datos["Servicios"]
        for Servicio in Servicios:
            for Adquisiciones in Servicio["Adquirido_por"]:
                Contador += Adquisiciones["Cantidad"]
            if Contador > Mayor:
                Mayor = Contador
                NombreServicio = Servicio["Nombre_Servicio"]
            Contador = 0
    print(f'Te recomendamos el Servicio "{NombreServicio}"')
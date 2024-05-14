import Modulos.ManejoExcepiciones
import Modulos.DatosYValidaciones
import Modulos.Menus

def CrearProductos(Datos):
    while True:
        Producto = {}
        Producto["Nombre_Producto"] = str(input("Nombre del Producto\n> "))
        Identidicador_Validado = PedirCodigoIdentificador()
        if IdentificadorNoRepetido(Identidicador_Validado, Datos):
            print("Identidicador Repetido")
            return Datos
        Producto["Codigo_Identificador"] = Identidicador_Validado
        Producto["Tipo"] = Modulos.DatosYValidaciones.ValidacionTipodeProducto()
        Producto["Descripcion"] = str(input("Ingrese una descripcion de el Producto\n> "))
        Producto["Marca"] = Modulos.DatosYValidaciones.ValidacionMarca()
        Producto["Precio"] = Modulos.DatosYValidaciones.ValidacionPrecios("Precio")
        Producto["Adquirido_por"] = []
        Datos["Productos"].append(Producto)
        print("Producto Creado")
        return Datos
    
def ListarProductos(Datos):
    Productos = Datos["Productos"]
    for Producto in Productos:
        print("Nombre del Producto: ", Producto["Nombre_Producto"])
        print("Codigo Producto: ", Producto["Codigo_Identificador"])
        print("Tipo de Producto: ", Producto["Tipo"])
        print("Descripcion: ", Producto["Descripcion"])
        print("Marca: ", Producto["Marca"])
        print("Precio: ", Producto["Precio"])
        print("")
        
def ActualizarProductos(Datos):
    Identidicador = PedirCodigoIdentificador()
    Productos = Datos["Productos"]
    for Producto in Productos:
        if Producto["Codigo_Identificador"] == Identidicador:
            print("Que Desea Actualizar".center(50))
            print("(1) Nombre del Producto".center(50))
            print("(2) Identificador".center(50))
            print("(3) Tipo".center(50))
            print("(4) Descripcion".center(50))
            print("(5) Marca".center(50))
            print("(6) Precio".center(50))
            print("(0) Volver".center(50))
            while True:
                choise = Modulos.Menus.Eleccion_Numerica()
                if choise == 1:
                    Producto["Nombre_Producto"] = str(input("Nombre del Producto\n> "))
                    print("Nombre Actualizado")
                    return Datos
                elif choise == 2:
                    Identidicador_Validado = PedirCodigoIdentificador()
                    if IdentificadorNoRepetido(Identidicador_Validado, Datos):
                        print("Identidicador Repetido")
                        return Datos
                    else:
                        Producto["Codigo_Identificador"] = Identidicador_Validado
                        print("Codigo Identificador Actualizado")
                        return Datos
                elif choise == 3:
                    Producto["Tipo"] = Modulos.DatosYValidaciones.ValidacionTipodeProducto()
                    print("Tipo de Producto Actualizado")
                    return Datos
                elif choise == 4:
                    Producto["Descripcion"] = str(input("Ingrese una descripcion de el Producto\n> "))
                    print("Descripcion Actualizada")
                    return Datos
                elif choise == 5:
                    Producto["Marca"] = Modulos.DatosYValidaciones.ValidacionMarca()
                    print("Marca Actualizada")
                    return Datos
                elif choise == 6:
                    Producto["Precio"] = Modulos.DatosYValidaciones.ValidacionPrecios("Precio")
                    print("Precio Actualizado")
                    return Datos
                elif choise == 0:
                    print("")
                    return Datos
                else:
                    print("Valor Invalido")
                    return Datos
    print("Identidicador No Encontrado")
    return Datos
    
def EliminarProducto(Datos):
    Identidicador = PedirCodigoIdentificador()
    Productos = Datos["Productos"]
    for Producto in Productos:
        if Producto["Codigo_Identificador"] == Identidicador:
            Productos.remove(Producto)
            Datos["Productos"] = Productos
            print("Producto Eliminado")
            return Datos
    print("Identidicador No ENcontrado".center(50, "="))
    return Datos
    
def PedirCodigoIdentificador():
    while True:
            print("Introduce Un Codigo Identificador: ")
            Identidicador = Modulos.Menus.Eleccion_Numerica()
            if Identidicador != 0 and Identidicador > 0:
                break
            else:
                print("Debe ser un Numero, Diferente a 0 y Positivo")
    return Identidicador

def IdentificadorNoRepetido(Identificador, Datos):
    Productos = Datos["Productos"]
    for Producto in Productos:
        if Producto["Codigo_Identificador"] == Identificador:
            return True
    return False

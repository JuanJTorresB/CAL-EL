import Modulos.CatalogoYRecomendaciones
import Modulos.GestionProductos
import Modulos.GestionVentas
import Modulos.GestionReportes
import Modulos.ManejoExcepiciones, Modulos.InicioSesion, Modulos.GestionUsuarios, Modulos.GestionServicios
import Modulos.Menus
import Modulos.ReclamosYSugerencias

UBI_DATOS = "Datos/UsuariosServiciosProductos.json"

def Menu_Inicial(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) SIGN IN".rjust(30))
        print("")
        print("")                               # Imprime las opciones del menu
        print("(2) SIGN UP".rjust(30))
        print("")
        print("")
        print("(3) SALIR".rjust(28))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Rol = Modulos.InicioSesion.SignIn(Datos)
            if  Rol == "Admin":
                return Rol
            elif Rol == "User":
                return Rol
            else:
                return 0
        elif choise == 2:
            Modulos.InicioSesion.SignUp(Datos)
            return "User"
        elif choise == 3:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
        
def Eleccion_Numerica():
    try:
        choise = int(input("> "))
        return choise
    except ValueError:
        print("Valor Invalido")
        Modulos.ManejoExcepiciones.LogExcepciones("Value Error", "42", "Menus.py")
    return(0)

def MenuAdmin(Datos):
    print("*"*50)
    print("")
    print("BIENVENIDO ADMIN".center(50))
    print("")
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Gestionar Usuarios".center(50))
        print("")
        print("")                               # Imprime las opciones del menu Admin
        print("(2) Gestionar Servicios".center(50))
        print("")
        print("")
        print("(3) Gestionar Productos".center(50))
        print("")
        print("")
        print("(4) Ver Reportes Comerciales".center(50))
        print("")
        print("")
        print("(5) Gestionar Ventas".center(50))
        print("")
        print("")
        print("(8) SALIR".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            MenuGestionarUsuarios(Datos)
        elif choise == 2:
            MenuGestionarServicios(Datos)
        elif choise == 3:
            MenuGestionarProductos(Datos)
        elif choise == 4:
            MenuReportesComerciales(Datos)
        elif choise == 5:
            MenuGestionarVentas(Datos)
        elif choise == 8:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuGestionarUsuarios(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Crear Perfiles de Usuarios".center(50))
        print("")
        print("")                                                        # Imprime las opciones del menu Gestionar Usuarios
        print("(2) Listar Perfiles de Usuarios".center(50))
        print("")
        print("")
        print("(3) Actualizar Perfil de Usuarios".center(50))
        print("")
        print("")
        print("(4) Eliminar Perfil de Usuarios".center(50))
        print("")
        print("")
        print("(5) VOLVER".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Datos = Modulos.GestionUsuarios.CrearPerfilesUsuarios(Datos)
        elif choise == 2:
            Modulos.GestionUsuarios.ListarPerfilesUsuarios(Datos)
        elif choise == 3:
            Datos = Modulos.GestionUsuarios.ActualizarPerfilesUsuarios(Datos)
        elif choise == 4:
            Datos = Modulos.GestionUsuarios.EliminarPerfilesUsuarios(Datos)
        elif choise == 5:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
        
def MenuGestionarServicios(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Crear Servicios".center(50))
        print("")
        print("")                                                        # Imprime las opciones del menu Gestionar Usuarios
        print("(2) Listar Servicios".center(50))
        print("")
        print("")
        print("(3) Actualizar Servicios".center(50))
        print("")
        print("")
        print("(4) Eliminar Servicios".center(50))
        print("")
        print("")
        print("(5) VOLVER".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Datos = Modulos.GestionServicios.CrearServicios(Datos)
        elif choise == 2:
            Modulos.GestionServicios.ListarServicios(Datos)
        elif choise == 3:
            Datos = Modulos.GestionServicios.ActualizarServicios(Datos)
        elif choise == 4:
            Datos = Modulos.GestionServicios.EliminarServicios(Datos)
        elif choise == 5:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuGestionarProductos(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Crear Productos".center(50))
        print("")
        print("")                                                        # Imprime las opciones del menu Gestionar Usuarios
        print("(2) Listar Productos".center(50))
        print("")
        print("")
        print("(3) Actualizar Productos".center(50))
        print("")
        print("")
        print("(4) Eliminar Productos".center(50))
        print("")
        print("")
        print("(5) VOLVER".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Datos = Modulos.GestionProductos.CrearProductos(Datos)
        elif choise == 2:
            Modulos.GestionProductos.ListarProductos(Datos)
        elif choise == 3:
            Datos = Modulos.GestionProductos.ActualizarProductos(Datos)
        elif choise == 4:
            Datos = Modulos.GestionProductos.EliminarProducto(Datos)
        elif choise == 5:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuGestionarVentas(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Registrar Nueva Venta Productos".center(50))
        print("")
        print("")                               # Imprime las opciones del menu Admin
        print("(2) Registrar Nueva Venta Servicios".center(50))
        print("")
        print("")
        print("(3) Listar Ventas Servicios".center(50))
        print("")
        print("")
        print("(4) Listar Ventas Productos".center(50))
        print("")
        print("")
        print("(5) Actualizar Ventas Servicios".center(50))
        print("")
        print("")
        print("(6) Actualizar Ventas Productos".center(50))
        print("")
        print("")
        print("(7) Volver".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Datos = Modulos.GestionVentas.RegistrarVentaProductos(Datos)
        elif choise == 2:
            Datos = Modulos.GestionVentas.RegistrarVentaServicios(Datos)
        elif choise == 3:
            Modulos.GestionVentas.ListarVentasServicios(Datos)
        elif choise == 4:
            Modulos.GestionVentas.ListarVentasProductos(Datos)
        elif choise == 5:
            Modulos.GestionVentas.ActualizarVentasServicios(Datos)
        elif choise == 6:
            Modulos.GestionVentas.ActualizarVentasProductos(Datos)
        elif choise == 7:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuReportesComerciales(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Cantidad de Productos Vendidos".center(50))
        print("")
        print("")                               # Imprime las opciones del menu Admin
        print("(2) Cantidad de Productos Servicios".center(50))
        print("")
        print("")
        print("(3) Producto Mas Vendido Por Ciudad".center(50))
        print("")
        print("")
        print("(4) Servicio Mas Vendido Por Ciudad".center(50))
        print("")
        print("")
        print("(5) Producto Mas Popular".center(50))
        print("")
        print("")
        print("(6) Sercivio Mas Popular".center(50))
        print("")
        print("")
        print("(7) Volver".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Modulos.GestionReportes.ContarCantidadVendidasProducto(Datos)
        elif choise == 2:
            Modulos.GestionReportes.ContarCantidadVendidasServicio(Datos)
        elif choise == 3:
            Modulos.GestionReportes.ContarProductosPorCiudad(Datos)
        elif choise == 4:
            Modulos.GestionReportes.ContarServiciosPorCiudad(Datos)
        elif choise == 5:
            Modulos.GestionReportes.ProductoMasPopular(Datos)
        elif choise == 6:
            Modulos.GestionReportes.ServicioMasPopular(Datos)
        elif choise == 7:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")

def MenuUser(Datos):
    print("*"*50)
    print("")
    print("BIENVENIDO USER".center(50))
    print("")
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Ver Catalogo".center(50))
        print("")
        print("")
        print("(2) Ver Recomendacion".center(50))
        print("")
        print("")
        print("(3) Poner Reclamo".center(50))
        print("")
        print("")
        print("(4) Poner Sugerencia".center(50))
        print("")
        print("")
        print("(5) SALIR".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            MenuVerCatalogo(Datos)
        elif choise == 2:
            "a"
        elif choise == 3:
            Datos = Modulos.ReclamosYSugerencias.RegistrarReclamos(Datos)
        elif choise == 4:
            Datos = Modulos.ReclamosYSugerencias.RegistrarSugerencias(Datos)
        elif choise == 5:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
            
def MenuVerCatalogo(Datos):
    while True:
        print("")
        print("*"*50)
        print("")
        print("Que Desea Hacer".center(50))
        print("")
        print("(1) Ver Servicios por tipo (Prepago, Postpago, Fibra Optica)".center(50))
        print("")
        print("")
        print("(2) Ver Productos por tipo (Celular, Televisor, Portatil)".center(50))
        print("")
        print("")
        print("(3) Volver".center(50))
        print("")
        choise = Eleccion_Numerica()           # Pide el input int
        if choise == 1:
            Modulos.CatalogoYRecomendaciones.CatalogoServicios(Datos)
        elif choise == 2:
            Modulos.CatalogoYRecomendaciones.CatalogoProductos(Datos)
        elif choise == 3:
            break
        elif choise == 0:
            print("")
        else:
            print("Valor Invalido")
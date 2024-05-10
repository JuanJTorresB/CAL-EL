import datetime

def LogExcepciones(Mensaje="Exception", Linea="Desconocida", Archivo="Desconocido"):
    UBI_REPORTE_EXCEPSIONES = "Datos/Reporte_Excepciones.txt"
    with open(UBI_REPORTE_EXCEPSIONES, "a") as file:
        file.write(f'\nMensaje de Excepcion "{Mensaje}", en la linea "{Linea}", en el archivo "{Archivo}" en la fecha {datetime.datetime.now()}')
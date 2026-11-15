from datos.db_config import conectar
from objetos.prestamo import Prestamo

def guardarPrestamo(pSocioId, pLibroId, pFecha, pVencimiento):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM socios WHERE id = %s", (pSocioId,))
    if not cursor.fetchone():
        print("ERROR: El socio no existe.")
        cursor.close()
        conn.close()
        return

    cursor.execute("SELECT disponibles FROM libros WHERE id = %s", (pLibroId,))
    libro_fila = cursor.fetchone()
    if not libro_fila:
        print("ERROR: El libro no existe.")
        cursor.close()
        conn.close()
        return

    disponibles = libro_fila[0]
    if disponibles <= 0:
        print("ERROR: No hay ejemplares disponibles de este libro.")
        cursor.close()
        conn.close()
        return

    cursor.execute("INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo, fecha_vencimiento) VALUES (%s, %s, %s, %s)",
                   (pSocioId, pLibroId, pFecha, pVencimiento))
    cursor.execute("UPDATE libros SET disponibles = disponibles - 1 WHERE id = %s", (pLibroId,))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Préstamo guardado !!!")

def traerPrestamos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, socio_id, libro_id, fecha_prestamo, fecha_vencimiento, fecha_devolucion FROM prestamos")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()
    return filas

def devolverPrestamo(pIdPrestamo, pFechaDevolucion):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT libro_id, fecha_devolucion FROM prestamos WHERE id = %s", (pIdPrestamo,))
    fila = cursor.fetchone()
    if not fila:
        print("ERROR: El préstamo no existe.")
        cursor.close()
        conn.close()
        return

    libro_id = fila[0]
    fecha_dev = fila[1]
    if fecha_dev is not None:
        print("ERROR: El préstamo ya fue devuelto anteriormente.")
        cursor.close()
        conn.close()
        return

    cursor.execute("UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s", (pFechaDevolucion, pIdPrestamo))
    cursor.execute("UPDATE libros SET disponibles = disponibles + 1 WHERE id = %s", (libro_id,))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Devolución registrada !!!")

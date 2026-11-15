from datos.db_config import conectar
from objetos.libro import Libro

def guardarLibro(pTitulo, pAutor, pAnio, pCantidad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor, anio, cantidad, disponibles) VALUES (%s, %s, %s, %s, %s)",
                   (pTitulo, pAutor, pAnio, pCantidad, pCantidad))
    conn.commit()
    cursor.close()
    conn.close()

def traerLibros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, anio, cantidad, disponibles FROM libros")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()
    return filas

def traerLibro(pIdLibro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, anio, cantidad, disponibles FROM libros WHERE id = %s", (pIdLibro,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    if fila:
        lib = Libro(fila[1], fila[2], fila[3], fila[4], fila[5])
        return lib
    return None

def modificarLibro(pTitulo, pAutor, pAnio, pCantidad, pId):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT cantidad, disponibles FROM libros WHERE id = %s", (pId,))
    actual = cursor.fetchone()
    if actual:
        cant_actual = actual[0]
        disp_actual = actual[1]
        prestados = cant_actual - disp_actual
        nuevo_disp = pCantidad - prestados
        if nuevo_disp < 0:
            print("ERROR: La nueva cantidad es menor a los ejemplares actualmente prestados.")
            cursor.close()
            conn.close()
            return
        cursor.execute("UPDATE libros SET titulo = %s, autor = %s, anio = %s, cantidad = %s, disponibles = %s WHERE id = %s",
                       (pTitulo, pAutor, pAnio, pCantidad, nuevo_disp, pId))
        conn.commit()
    cursor.close()
    conn.close()

def borrarLibro(pId):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM prestamos WHERE libro_id = %s", (pId,))
    count = cursor.fetchone()[0]
    if count > 0:
        print("ERROR: No se puede borrar el libro porque tiene préstamos registrados.")
        cursor.close()
        conn.close()
        return
    cursor.execute("DELETE FROM libros WHERE id = %s", (pId,))
    conn.commit()
    cursor.close()
    conn.close()

from datos.db_config import conectar
from objetos.socio import Socio

def guardarSocio(pNom, pApe):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO socios (nombre, apellido) VALUES (%s, %s)", (pNom, pApe))
    conn.commit()
    cursor.close()
    conn.close()

def traerSocios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido FROM socios")
    filas = cursor.fetchall()
    cursor.close()
    conn.close()
    return filas

def traerSocio(pIdSocio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido FROM socios WHERE id = %s", (pIdSocio,))
    fila = cursor.fetchone()
    cursor.close()
    conn.close()
    if fila:
        soc = Socio(fila[1], fila[2])
        return soc
    return None

def modificarSocio(pNom, pApe, pId):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE socios SET nombre = %s, apellido = %s WHERE id = %s", (pNom, pApe, pId))
    conn.commit()
    cursor.close()
    conn.close()

def borrarSocio(pId):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM prestamos WHERE socio_id = %s", (pId,))
    count = cursor.fetchone()[0]
    if count > 0:
        print("ERROR: No se puede borrar el socio porque tiene préstamos registrados.")
        cursor.close()
        conn.close()
        return
    cursor.execute("DELETE FROM socios WHERE id = %s", (pId,))
    conn.commit()
    cursor.close()
    conn.close()

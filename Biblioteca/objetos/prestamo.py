class Prestamo:
    def __init__(self, pSocioId, pLibroId, pFecha, pVencimiento, pFechaDevolucion=None):
        self.SocioId = pSocioId
        self.LibroId = pLibroId
        self.Fecha = pFecha
        self.Vencimiento = pVencimiento
        self.FechaDevolucion = pFechaDevolucion

    def verDatos(self):
        print("ID Socio: ", self.SocioId)
        print("ID Libro: ", self.LibroId)
        print("Fecha Préstamo: ", self.Fecha)
        print("Fecha Vencimiento: ", self.Vencimiento)
        dev = self.FechaDevolucion if self.FechaDevolucion else "Pendiente"
        print("Fecha Devolución: ", dev)

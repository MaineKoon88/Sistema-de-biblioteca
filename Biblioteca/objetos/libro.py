class Libro:
    def __init__(self, pTitulo, pAutor, pAnio, pCantidad, pDisponibles=None):
        self.Titulo = pTitulo
        self.Autor = pAutor
        self.Anio = pAnio
        self.Cantidad = pCantidad
        self.Disponibles = pDisponibles if pDisponibles is not None else pCantidad

    def verDatos(self):
        print("Título: ", self.Titulo)
        print("Autor: ", self.Autor)
        print("Año: ", self.Anio)
        print("Cantidad Total: ", self.Cantidad)
        print("Disponibles: ", self.Disponibles)

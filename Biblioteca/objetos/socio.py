class Socio:
    def __init__(self, pNombre, pApellido):
        self.Nombre = pNombre
        self.Apellido = pApellido

    def verDatos(self):
        print("Nombre: ", self.Nombre)
        print("Apellido: ", self.Apellido)

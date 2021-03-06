
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    # Se redefine el metodo avanza
    def avanza(self):
        print('Ando moviendome en mi bicicleta')

def main():
    persona = Persona('Jhony')
    persona.avanza()

    ciclista = Ciclista('Andres')
    ciclista.avanza()

if __name__ == '__main__':
    main()
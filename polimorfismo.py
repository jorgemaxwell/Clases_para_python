
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza (self):
        print("Ando Caminando")


class Ciclista(Persona):
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print ("Ando moviendome en mi bicileta")

def main():
    persona = Persona("David")
    persona.avanza()

    ciclista= Ciclista("daniel")
    ciclista.avanza()

if __name__ == "__main__":
    main()


class Automovil:

    def __init__(self, modelo, marca, color,gasolina=20):
        self.modelo = modelo
        self.modelo = marca
        self.color = color
        self._estado = "en_reposo"
        self._motor = motor(cilindros = 4)
        self.gasolina = gasolina
        self._cojineria = "Cuero"
    
    def acelerar(self, tipo = "despacio"):
        if tipo == "rapida":
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = "acelerando"
        self.gasolina -= cantidad
        

class motor:

    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        gasolina += cantidad
        self.gasolina -= cantidad


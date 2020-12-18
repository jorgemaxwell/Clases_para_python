class area:                                #DEFINICION DE CLASES 
    def __init__(self, base, altura):      #CONSTRUCTOR DE MI CLASE
        self.base = base                   #INICIALIZACION DE MIS VARIABLES DE LA CLASE     
        self.altura = altura

    def calcular(self):       #METODO CALCULAR DE MI CLASE,DEBE CALCULAR EL AREA
        a = (self.base * self.altura)/2     #ASUMIENDO QUE SEA UN TRIANGULO
        return a

if __name__ == "__main__":                 #ENTRY POINT 
    triangulo1 = area(5 , 5)                # INSTANCIA
    print(triangulo1.calcular())
                  
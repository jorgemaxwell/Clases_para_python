class coordenada:               #DECLARO MI CLASE COORDENADA               
    def __init__(self, x, y):   #CONSTRUCTOR DE MI CLASE
        
        self.x= x               #INICIALIZO LAS VARIABLES QUE VA A UTILIZAR MI CLASE 
        self.y= y               #EN ESTE CASO X y Y.
    
    def distancia (self, otra_coordenada):         #DEFINO MI PRIMER METODO EL CUAL ME DEFINE 
        x_diff= (self.x - otra_coordenada.x)**2    #LAS OPERACIONES QUE VA A REALIZAR MI CLASE
        y_diff= (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5               #RETURN EL RESULTADO DE LA OPERACION 

if __name__ == "__main__":                          #ENTRY POINT
    coord_1= coordenada (3, 30)                     #DEFINO MI PRIMERA INSTANCIA 
    coord_2= coordenada (4, 8)                      #DEFINO MI SEGUNDA INSTANCIA
    print(coord_1.distancia(coord_2))               #PRINT.
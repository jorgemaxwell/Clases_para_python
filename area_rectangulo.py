class calcula_area:
    
    def __init__(self, l):
        self.l = l
    
    def area (self):
        return self.l * self.l

if __name__ == "__main__":
    
    rectangulo1= calcula_area(5) 
    print(rectangulo1.area())
    
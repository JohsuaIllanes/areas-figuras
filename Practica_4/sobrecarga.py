class Area:
    def area(self, *args):
        
        if len(args) == 1: 
            radio = args[0]
            return 3.1416 * radio ** 2 

        elif len(args) == 2: 
            base, altura = args
            return base * altura

        elif len(args) == 3 and isinstance(args[2], float): 
            base_mayor, base_menor, altura = args
            return ((base_mayor + base_menor) * altura) / 2 

        elif len(args) == 3 and isinstance(args[2], int): 
            lado, apotema, lados = args
            return (lados * lado * apotema) / 2

        else:
            return "Error: Número de parámetros incorrecto"

calc = Area()
print("Área del círculo:", calc.area(5)) 
print("Área del rectángulo:", calc.area(4, 6))  
print("Área del triángulo rectángulo:", calc.area(3, 6)) 
print("Área del trapecio:", calc.area(6, 4, 5.0))  
print("Área del pentágono:", calc.area(4, 5, 5))  

class Area {
    
    public double area(double radio) {
        return Math.PI * radio * radio; 
    }
    public double area(double base, double altura) {
        return base * altura; 
    }

    public double area(double baseMayor, double baseMenor, double altura) {
        return ((baseMayor + baseMenor) * altura) / 2; 
    }

    public double area(double lado, double apotema, int lados) {
        return (lados * lado * apotema) / 2;
    }

    public static void main(String[] args) {
    
        Area calc = new Area();

        System.out.println("Área del círculo: " + calc.area(5)); 
        System.out.println("Área del rectángulo: " + calc.area(4, 6)); 
        System.out.println("Área del trapecio: " + calc.area(6, 4, 5)); 
        System.out.println("Área del pentágono: " + calc.area(4, 5, 5)); 
        
    }
}

from figuras import *


p1 = punto(5,5)
p2 = punto(5,10)
p = punto (10,1)

cuadrado = Cuadrado (p1, p2)
circulo =  Circulo (p1, p2)
triangulo = Triangulo (p1,p)


cuadrado.calcular_area ()
circulo.calcular_area ()
cuadrado.calcular_perimetro ()
circulo.calcular_perimetro ()
triangulo.calcular_area ()


print cuadrado.area
print cuadrado.perimetro
print circulo.area
print circulo.perimetro
print triangulo.area



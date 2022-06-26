# Comprobando si un triángulo es equilátero

# Longitud de los lados
x = int()
y = int()
z = int()

# Un lado nunca puede superar la suma de los otros dos
if x >= y+z or y >= x+z or z >= x+y:
    print("The triangle does not exist")
elif x==y and x==z:
    print ("Equilateral")
elif x==y or x==z or y==z:
    print ("Isosceles")
else:
    print("Obtuse")
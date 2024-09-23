import math
x = float(input("введите объем шара: " ))
r = (3 * x / (4 * math.pi)) ** (1/3) 
print("радиус фигуры = ",  round(r,2))
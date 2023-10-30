import math
def triangle_area(a, b, c):
    return (abs((a + b + c) / 2) * math.sqrt(math.pow((a / 2), 2) - math.pow(math.fabs(((b + c) / 2) - a) / 2, 2)))
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
area = triangle_area(a, b, c)
print("Площадь треугольника:", area)

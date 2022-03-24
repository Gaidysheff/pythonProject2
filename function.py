
# from math import pi
#
#
# def Cicle(R):
#     Square_cycle = pi * R ** 2
#     return Square_cycle
#
# def Square_rectangle(a, b):
#     Square_rectangle = a * b
#     return Square_rectangle
#
#
#
# if __name__ == '__main__':
#     print(f"Число Пи = {pi}")
#     R = int(input("Введите радиус круга: "))
#     a = int(input("Введите первую сторону прямоугольника: "))
#     b = int(input("Введите вторую сторону прямоугольника: "))
#     c1 = Cicle()
#     r1 = Square_rectangle()
#     print(f"площать круга = {c1}")
#     print(f"площать прямоугольника = {r1}")



from main import *


def main():
    r = int(input('Введите радиус круга:\n'))

    a = int(input('Введите длину прямоугольника:\n'))
    b = int(input('Введите ширину прямоугольника:\n'))

    if circle_area(r) > rect_area(a, b):
           print('Площадь круга больше')
    else:
           print('Площадь прямоугольника больше')


main()
c1 = circle_area()
r1 = rect_area()

print(f"площать круга = {c1}")
print(f"площать прямоугольника = {r1}")
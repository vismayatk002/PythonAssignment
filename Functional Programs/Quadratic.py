"""

    @Author : Vismaya
    @Date   : 2021-10-20 01:35
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 02:04
    @Title : Solution of Quadratic equation

"""

import math


def calc_root(a, b, c):
    root1 = 0
    root2 = 0
    delta = (pow(b, 2) - (4 * a * c))
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        root1 = round(root1, 2)
        root2 = round(root2, 2)
        print("Roots of Equation x1 : ", root1,  " ,  x2 : ", root2)
    elif delta == 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root1 = round(root1, 2)
        print("Roots of Equation x1 : ", root1)
    else:
        print("Roots of Equation is imaginary")


fno = int(input("Enter first number : "))
sno = int(input("Enter second number  : "))
tno = int(input("Enter third number  : "))

calc_root(fno, sno, tno)

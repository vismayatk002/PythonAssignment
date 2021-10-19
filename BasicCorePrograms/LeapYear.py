"""

    @Author : Vismaya
    @Date   : 2021-10-18 10:28
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 11:19
    @Title : Check given year is Leap year or not

"""

import math


def is_leap_year(num):

    if num % 4 == 0:
        flag = 1
    else:
        flag = 0

    return flag;


year = int(input("Enter the Year : "))
digits = int(math.log10(year))+1

if digits == 4:
    if is_leap_year(year) == 1:
        print("Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Invalid Year")
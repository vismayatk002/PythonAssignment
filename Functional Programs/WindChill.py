"""

    @Author : Vismaya
    @Date   : 2021-10-20 01:35
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 01:47
    @Title : Calculate Wind chill

"""

import sys
import math


def calc_windchill(t, v):
    if t < 50 and 3 < v < 120:
        windchill = (35.74 + (0.6215 * t) + (((t * 0.4275) - 35.75) * (pow(v, 0.16))))
        windchill = round(windchill, 2)
        print("Wind Chill : ", windchill)
    else:
        print("Invalid Input")


temp = int(sys.argv[1])
speed = int(sys.argv[2])

calc_windchill(temp, speed)

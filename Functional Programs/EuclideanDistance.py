"""

    @Author : Vismaya
    @Date   : 2021-10-20 01:08
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 01:30
    @Title : Calculate  Euclidean distance

"""

import sys
import math


def get_distance(a, b):
    distance = (math.sqrt(pow(x, 2) + pow(y, 2)))
    return distance


x = int(sys.argv[1])
y = int(sys.argv[2])
dist = get_distance(x, y)
dist = round(dist, 2)
print("Euclidean distance : ", dist)

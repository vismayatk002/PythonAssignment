"""

    @Author : Vismaya
    @Date   : 2021-10-18 11:19
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 01:10
    @Title : Table of Power of 2

"""

import sys


def power_of_two(num):
    for i in range(1, num+1):
        power = pow(2, i)
        print("2^", i, " = ", power)


number = int(sys.argv[1])
print(number)

if 0 <= number < 31:
    power_of_two(number)
else:
    print("Invalid Range")
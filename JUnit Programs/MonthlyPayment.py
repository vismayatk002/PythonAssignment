"""

    @Author : Vismaya
    @Date   : 2021-10-20 08:15
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 04:47
    @Title : Monthly Payment using Principal amount(P), year to pay off(Y),  per cent
            interest compounded monthly(R)

"""

import sys
import math


class Payment:
    @staticmethod
    def calc_payment(Y, P, R):
        n = 12 * Y
        r = R / 1200
        payment = (P * r) / (1 - pow((1 + r), (-n)))
        return payment


pay = Payment()
year = int(sys.argv[1])
principalAmount = int(sys.argv[2])
interest = int(sys.argv[3])
result = pay.calc_payment(year, principalAmount, interest)
result = round(result, 2)
print("Monthly Payment : ", result)
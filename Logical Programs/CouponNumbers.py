"""

    @Author : Vismaya
    @Date   : 2021-10-20 03:59
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 06:55
    @Title : Coupon Numbers

"""

import random


class CouponNumber:
    @staticmethod
    def coupon_no(self, couponCount):
        couponArr = []
        count = 0
        while count <= couponCount:
            number = random.randint(10, 100)
            if number not in couponArr:
                couponArr.append(number)
                print(number)
                count += 1


noOfCoupon = int(input("Enter the number of coupon number : "))
coupon = CouponNumber()
coupon.coupon_no(noOfCoupon)

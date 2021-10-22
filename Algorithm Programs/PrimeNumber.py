"""

    @Author : Vismaya
    @Date   : 2021-10-20 12:09
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 12:46
    @Title : Prime numbers in a range

"""


class Prime:
    def is_prime(self):
        min = 1
        max = 1000
        print("Prime numbers ")
        for i in range(min, max):
            flag = 1
            for j in range(2, i):
                if i % j == 0:
                    flag = 0

            if flag == 1:
                print(i)


prime_obj = Prime()
prime_obj.is_prime()
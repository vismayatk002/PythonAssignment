"""

    @Author : Vismaya
    @Date   : 2021-10-18 09:12
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 10:54
    @Title : Decimal to Binary Conversion

"""


class Conversion:
    @staticmethod
    def dec_to_bin(dec):
        if dec > 0:
            Conversion.dec_to_bin(int(dec / 2))
            print(dec % 2, end='')


decimal = int(input("Enter a decimal number \n"))
convert = Conversion()
convert.dec_to_bin(decimal)

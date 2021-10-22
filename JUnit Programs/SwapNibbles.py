"""

    @Author : Vismaya
    @Date   : 2021-10-18 10:54
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 10:54
    @Title : Swap nibbles and find new Decimal number

"""


class Swap:
    @staticmethod
    def dec_to_bin(dec):
        if dec > 0:
            Swap.dec_to_bin(int(dec / 2))
            bin_num = dec % 2
            return bin_num

    @staticmethod
    def nibbles():
        decimal = int(input("Enter a decimal number \n"))
        bin_no = Swap.dec_to_bin(decimal)
        new_bin = bin_no[4:8] + bin_no[0:4]
        print("Swapped binary number: ", end='')
        print(new_bin)
        new_num = int(new_bin, 2)
        print("New Decimal number formed by swapping: ", end='')
        return new_num

    @staticmethod
    def check_power(n):
        if n == 0:
            return 0
        while n != 1:
            if n % 2 != 0:
                return 0
            n = n // 2
        return 1


new_no = Swap.nibbles()
result = Swap.check_power(new_no)
if result == 1:
    print('Yes')
else:
    print('No')


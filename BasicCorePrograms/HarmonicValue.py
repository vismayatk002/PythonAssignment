"""

    @Author : Vismaya
    @Date   : 2021-10-18 11:39
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 11:59
    @Title : Find the Nth Harmonic value

"""


def harmonic_sum(num):
    result = 0
    for i in range(1, num+1):
        result += 1 / i
    return result;


number = int(input("Enter the Number : "))

if number != 0:
    value = harmonic_sum(number)
    value = round(value, 2)
    print("Harmonic value : ", value)
else:
    print("Invalid")

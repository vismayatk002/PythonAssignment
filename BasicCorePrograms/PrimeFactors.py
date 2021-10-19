"""

    @Author : Vismaya
    @Date   : 2021-10-18 11:39
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 12:52
    @Title : Prime factors of a number

"""


def is_prime(num):
    flag = 0
    for j in range(2, num):
        if num % j == 0:
            flag = 1
            break
        j += 1

    return flag;


number = int(input("Enter the Number : "))

i = 2
print("Prime factors : ")
while i <= number:
    if number % i == 0:
        result = is_prime(i)
        if result == 0:
            print(i)
    i += 1

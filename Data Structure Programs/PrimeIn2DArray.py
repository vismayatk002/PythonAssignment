"""

    @Author : Vismaya
    @Date   : 2021-10-20 12:46
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 01:24
    @Title : Store Prime numbers in a 2D array

"""


class Prime:
    def is_prime(self, min, max):
        prime_arr = []
        for i in range(min, max):
            flag = 1
            for j in range(2, i):
                if i % j == 0:
                    flag = 0

            if flag == 1:
                prime_arr.append(i)

        return prime_arr


prime_obj = Prime()
arr = []
for i in range(0, 1000, 100):
    result_Arr = prime_obj.is_prime(i, i+100)
    arr.append(result_Arr)

print(arr, end=" ")
print()



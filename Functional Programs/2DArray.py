"""

    @Author : Vismaya
    @Date   : 2021-10-19 07:59
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-19 12:22
    @Title : Read values and print 2D array

"""


def arr_func():
    arr = []
    print("Enter the values")
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input()))
        arr.append(a)

    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()


m = int(input("Enter the number of rows : "))
n = int(input("Enter the number of columns : "))

arr_func()
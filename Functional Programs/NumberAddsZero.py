"""

    @Author : Vismaya
    @Date   : 2021-10-20 11:48
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 01:10
    @Title : Sum of three numbers adds to zero

"""


def find_triples(arr=[]):
    triplescount = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplescount += 1

    if triplescount == 0:
        print("Array doesn't have triples")
    else:
        print("Triples count : ", triplescount)


count = int(input("Enter the count : "))
array = []
print("Enter the values")
for i in range(0, count):
    array.append(int(input()))
print(array)

find_triples(array)
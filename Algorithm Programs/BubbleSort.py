"""

    @Author : Vismaya
    @Date   : 2021-10-20 07:36
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 07:47
    @Title : Bubble Sort

"""

arr = []


def bubble_sort():
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted array : ", arr)


num = int(input("Enter the number of elements to be insert : "))
print("Enter the elements : ")
for j in range(num):
    arr.append(input())
print("Unsorted Array : ", arr)

bubble_sort()

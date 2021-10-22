"""

    @Author : Vismaya
    @Date   : 2021-10-20 02:23
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 07:36
    @Title : Insertion Sort

"""

arr = []


def insertion_sort():
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print("Sorted Array : ", arr)


num = int(input("Enter the number of elements to be insert : "))
print("Enter the elements : ")
for j in range(num):
    arr.append(input())
print("Unsorted Array : ", arr)
insertion_sort()
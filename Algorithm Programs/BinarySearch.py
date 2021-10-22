"""

    @Author : Vismaya
    @Date   : 2021-10-20 02:23
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 03:15
    @Title : Binary Search

"""


def binary_search(word_arr, n):
    low = 0
    high = len(word_arr) - 1
    while low <= high:
        mid = int((high + low) / 2)
        if word_arr[mid] < n:
            low = mid + 1
        elif word_arr[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1


num = int(input("Enter the number of words to be insert : "))
print("Enter the words : ")
words_arr = []
for j in range(num):
    words_arr.append(input())

print(words_arr)
words_arr.sort()
word = input("Which word you want to search? : ")
result = binary_search(words_arr, word)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")

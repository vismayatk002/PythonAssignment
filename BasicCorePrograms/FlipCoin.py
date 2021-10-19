"""

    @Author : Vismaya
    @Date   : 2021-10-18 09:36
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 10:27
    @Title : Flip coin and print percentage of Head & Tail

"""
import random

number = int(input("Enter the Number of times to flip coin : "))
i = 0
headCount = 0
tailCount = 0
for i in range(number+1):
    randomNo = random.uniform(0, 1)
    randomNo = round(randomNo, 2)
    if randomNo > 0:
        if randomNo > 0.5:
            headCount += 1
        else:
            tailCount += 1
    else:
        print("Invalid")

percentOfHead = float((headCount * 100) / number)
percentOfHead = round(percentOfHead, 2)
percentOfTail = float((tailCount * 100) / number)
percentOfTail = round(percentOfTail, 2)

print("Percentage of Head : ", percentOfHead , "%")
print("Percentage of Tail : ", percentOfTail , "%")
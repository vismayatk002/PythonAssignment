"""

    @Author : Vismaya
    @Date   : 2021-10-18 06:00
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 06:55
    @Title : Gambler bet

"""

import random

head = 1
tail = 0


def generate_rand_no():
    randomNo = random.uniform(0, 1)
    randomNo = round(randomNo, 2)
    if randomNo > 0.5:
        return head
    else:
        return tail


stake = int(input("Enter the holding amount : "))
goal = int(input("Enter the goal amount : "))
numOfTimes = int(input("Enter the Number of times to play the game : "))
count = 0
winCount = 0
lossCount = 0

while stake != 0 and goal != stake and count != numOfTimes:
    print("Select Head or Tail")
    option = int(input("Press 1 for Head and 0 for Tail : "))
    count += 1

    if generate_rand_no() == option:
        stake += 1
        winCount += 1
    else:
        stake -= 1
        lossCount += 1

print("Numbers of Wins : ", winCount)
perOfWin = (winCount * 100) / count
perOfLoss = (lossCount * 100) / count

print("Percentage of Win : ", perOfWin)
print("Percentage of Loss : ", perOfLoss)
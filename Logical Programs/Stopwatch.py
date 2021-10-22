"""

    @Author : Vismaya
    @Date   : 2021-10-20 02:39
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 04:47
    @Title : Stopwatch

"""

import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    hours = round(hours, 2)
    mins = round(mins, 2)
    sec = round(sec, 2)

    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


input("Press Enter to start")
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
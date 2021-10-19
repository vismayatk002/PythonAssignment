"""

    @Author : Vismaya
    @Date   : 2021-10-18 09:09
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 09:32
    @Title : Replace username to string

"""

userName = input("Enter the user name : ")
if len(userName) >= 3:
    print("Hello " + userName + ", How are you?")
else:
    print("User name have minimum three characters !")

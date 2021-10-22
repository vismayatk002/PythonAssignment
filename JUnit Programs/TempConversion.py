"""

    @Author : Vismaya
    @Date   : 2021-10-18 05:47
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-18 08:10
    @Title : Temperature Conversion

"""


def celsius_to_fahren(no):
    result = (no * 9 / 5) + 32
    return result


def fahren_to_celsius(no):
    result = (no - 32) * 5 / 9
    return result


print("1.Celsius to Fahrenheit(Press 1) \n2.Fahrenheit to Celsius(Press 2)")
option = int(input("Choose your option : "))
if option == 1:
    num = int(input("Enter the value(in °C) : "))
    print("Celsius to Fahrenheit : ", celsius_to_fahren(num))
else:
    num = int(input("Enter the value(in °F) : "))
    print("Fahrenheit to Celsius : ", fahren_to_celsius(num))


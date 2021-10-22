"""

    @Author : Vismaya
    @Date   : 2021-10-20 10:41
    @Last Modified by : Vismaya
    @Last Modified time : 2021-10-20 11:57
    @Title : Anagram Detection

"""


class Anagram:
    @staticmethod
    def are_anagram(s1, s2):
        if s1 == s2:
            return 1
        else:
            return 0


string1 = input("Enter the first string : ")
str_array1 = [char for char in string1]
str_array1.sort()
str1 = "".join(str_array1)

string2 = input("Enter thr second string : ")
str_array2 = [char for char in string2]
str_array2.sort()
str2 = "".join(str_array2)

anagram = Anagram()
result = anagram.are_anagram(str1, str2)
if result == 1:
    print("Two strings are Anagram")
else:
    print("Two strings are not Anagram")
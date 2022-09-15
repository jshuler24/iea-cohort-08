#! /usr/bin/python3
"""
final_answer = 0
romans_to_arabic = { 
    'M': '1000', 
    'D': '500', 
    'C': '100', 
    'L': '50' ,
    'X': '10' ,
    'V': '5' ,
    'I': '1'
}
user_conversion = input('What would you like to convert to arabic from roman?')
for word in (user_conversion.split()):
    final_answer = final_answer + int(romans_to_arabic[word])
print(final_answer)
"""

#User Roman Numerial input
roman = input("Please type a Roman Numeral ")

class Solution(object):

#calculation(s)
    def romanToInt(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1
        return num

#output
ob1 = Solution()
print(ob1.romanToInt(roman))
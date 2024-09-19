#!/usr/bin/python


import os


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            sub_string = s
        else:
            sub_string = "Not a Palindrome"
        return sub_string


    def isPalindrome(self, s:str) -> bool:
        length = len(s)
        if length % 2 == 0:
            first = s[0:length // 2]
            last = s[length // 2::]
        else:
            first = s[0:length // 2]
            last = s[length // 2 + 1::]
        print("First:" + first +  " Last: " + last)
        if first == last[::-1]:
            return True
        else:
            return False


def main():


    test = Solution()
    print("Test 1: "+ str(test.isPalindrome("babad")))
    print("Test 2: "+ str(test.isPalindrome("cbbd")))
    print("Test 3: "+ str(test.isPalindrome("d")))






if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
        os._exit(1)


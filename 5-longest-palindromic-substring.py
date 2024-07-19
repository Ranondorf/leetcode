#!/usr/bin/python


import os


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "b"
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
        if first == last[::-1]:
            return True
        else:
            return False


def main():


    test = Solution()
    print("Test 1: "+ test.longestPalindrome("babad"))
    print("Test 2: "+ test.longestPalindrome("cbbd"))






if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
        os._exit(1)


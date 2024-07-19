#!/usr/bin/python


import os


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_length = 0
        symbol_list = []
        i = 0
        while(i < len(s) and len(s) -i + 1 > max_length):
            for j in range(i, len(s)):
                if s[j] not in symbol_list:
                    current_length += 1
                    symbol_list.append(s[j])
                    if current_length > max_length:
                        max_length = current_length
                else:
                    current_length = 0
                    symbol_list = []
                    break
            i += 1
        return max_length


def main():


    test = Solution()
    print("Test 1: "+ str(test.lengthOfLongestSubstring("abcabcbb")))
    print("Test 2: "+ str(test.lengthOfLongestSubstring("bbbbb")))
    print("Test 3: "+ str(test.lengthOfLongestSubstring("pwwkew")))
    print("Test 4: "+ str(test.lengthOfLongestSubstring("jbpnbwwd")))





if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
        os._exit(1)


#!/usr/bin/python


import os


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    pass
                elif nums[i] + nums[j] == target:
                    return [i,j]


def main():


    test = Solution()
    print("Test 1: "+ str(test.twoSum([2,7,11,15], 9)))
    print("Test 2: "+ str(test.twoSum([3,2,4], 6)))
    print("Test 3: "+ str(test.twoSum([3,3], 6)))






if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
        os._exit(1)


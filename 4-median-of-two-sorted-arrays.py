#!/usr/bin/python


import os


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)
        if length % 2 == 1:
            median = nums3[length // 2]
        else:
            median = (nums3[int(length / 2)] + nums3[int(length / 2 - 1)])/2
        return median


def main():


    test = Solution()
    print("Test 1: "+ str(test.findMedianSortedArrays([1,3], [2])))
    print("Test 2: "+ str(test.findMedianSortedArrays([1,2], [3,4])))






if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
        os._exit(1)


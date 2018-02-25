#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 21:14
# @Author  : JiangPeng
# @File    : 26.Remove Duplicates from Sorted Array.py

'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

'''
去除有序数组重复项，且不增加数组空间
解题思路：采用快慢指针，初始指向第一个数字。如果两个两个数字相同，快指针加1，慢指针原地不动；不同快慢指针均加1 。
快指针走完后 慢指针加1 即 数组中不同数字的个数。将后一个元素 填入 前一个重复元素的位置
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j = j+1
                nums[j] = nums[i]
        print(nums)
        return j + 1



if __name__ == '__main__':
    a = Solution().removeDuplicates([1,2,2,3,4,4,7])
    print(a);
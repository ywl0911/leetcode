#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-2-26 下午11:14
# @Author  : ywl
# @File    : 4.py
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_new = []
        while len(nums1) != 0 or len(nums2) != 0:

            if len(nums1) == 0:
                nums_new.append(nums2[0])
                nums2.remove(nums2[0])
                continue

            if len(nums2) == 0:
                nums_new.append(nums1[0])
                nums1.remove(nums1[0])
                continue

            if nums1[0] <= nums2[0]:
                nums_new.append(nums1[0])
                nums1.remove(nums1[0])
            else:
                nums_new.append(nums2[0])
                nums2.remove(nums2[0])
        if len(nums_new) % 2 == 1:
            return nums_new[len(nums_new) / 2]
        else:
            return (nums_new[len(nums_new) / 2 - 1] + nums_new[len(nums_new) / 2]) / 2.


s = Solution()
print  s.findMedianSortedArrays([], [1])

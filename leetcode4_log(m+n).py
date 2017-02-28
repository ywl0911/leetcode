class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total=(len(nums1) + len(nums2))
        if total%2==1:
            return self.find_k_small_arry(nums1,len(nums1),nums2,len(nums2),int((total+1)/2))
        else:
            a=self.find_k_small_arry(nums1,len(nums1),nums2,len(nums2),int(total/2))
            b=self.find_k_small_arry(nums1,len(nums1),nums2,len(nums2),int(total/2+1))
            return (a+b)/2
    def find_k_small_arry(self,nums1,nums1_len,nums2,nums2_len,k):
        if nums1_len>nums2_len:
            return self.find_k_small_arry(nums2,nums2_len,nums1,nums1_len,k)
        if k>nums1_len+nums2_len:
            return False
        if nums1_len==0:
            return nums2[k-1]
        if k==1:
            return min(nums1[0],nums2[0])


        new_1=min(int(k/2),nums1_len)
        new_2=k-new_1

        if nums1[new_1-1]==nums2[new_2-1]:
            return nums1[new_1-1]
        elif nums1[new_1-1]>nums2[new_2-1]:
            return self.find_k_small_arry(nums1,nums1_len,nums2[new_2:],nums2_len-new_2,k-new_2)
        else:
            return self.find_k_small_arry(nums1[new_1:],nums1_len-new_1,nums2,nums2_len,k-new_1)


s=Solution()
print(s.findMedianSortedArrays([1,3],[4]))
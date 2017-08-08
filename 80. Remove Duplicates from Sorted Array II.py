class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = None
        current_count = 0
        length = 0
        i = 0
        while i < len(nums):
            if nums[i] == current:
                #                 print i
                #                 print current
                #                 print current_count
                #                 print '>>'

                current_count += 1
                if current_count <= 2:
                    length += 1
                    i += 1
                else:
                    del nums[i]
                    continue
            else:
                current = nums[i]
                current_count = 1
                length += 1
                i += 1

        return length

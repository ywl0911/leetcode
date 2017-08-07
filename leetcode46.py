class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        ready_list = []
        self.dfs(nums, ready_list)
        return self.result

    def dfs(self, nums, ready_list):
        if len(ready_list) == len(nums):
            self.result.append(ready_list[:])

        for i in nums:
            if i in ready_list:
                continue
            ready_list.append(i)
            self.dfs(nums, ready_list)
            ready_list.pop()

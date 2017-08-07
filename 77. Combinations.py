class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        nums = list(range(1, n + 1))
        self.dfs(nums, k, [])
        return self.result

    def dfs(self, nums, k, ready_list):
        if len(ready_list) == k:
            self.result.append(ready_list[:])
            return
        for i in range(len(nums)):
            a = nums[:]
            ready_list.append(nums[i])
            self.dfs(a[i + 1:], k, ready_list)
            ready_list.pop()
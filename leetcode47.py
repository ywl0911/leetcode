class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        ready_list = []
        nums.sort()
        ready_index = [0 for i in range(len(nums))]
        last = None
        self.dfs(nums, ready_list, ready_index)
        return self.result

    def dfs(self, nums, ready_list, flag):
        if len(ready_list) == len(nums):
            self.result.append(ready_list[:])

        last = None

        for i in range(len(nums)):
            if flag[i] == 1:
                continue
            if nums[i] == last:
                continue

            flag[i] = 1
            ready_list.append(nums[i])
            self.dfs(nums, ready_list, flag)
            last = ready_list.pop()
            flag[i] = 0


s = Solution()
print(s.permute([1, 2, 1]))

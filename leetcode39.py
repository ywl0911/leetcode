class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        candidates = sorted(candidates)
        self.dfs(candidates, [], target, 0)

        return self.result

    def dfs(self, candidates, read_list, target, last):
        if target == 0:
            self.result.append(read_list[:])  # a[:]是传值，a是传址
        if target < candidates[0]:
            return

        for i in candidates:
            if i > target:
                return
            # if i < last:
            #     continue
            read_list.append(i)
            self.dfs(candidates, read_list, target - i, i)
            read_list.pop()


b = Solution()
print(b.combinationSum([2, 3, 6, 7], 7))

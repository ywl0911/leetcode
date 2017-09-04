class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    # a dfs problem
    def subsetsWithDup(self, S):
        S.sort()
        ready_list = []
        self.result = []
        self.dfs(ready_list, 0, S)
        return self.result

    def dfs(self, read_list, start, S):

        if read_list in self.result:
            return
        self.result.append(read_list[:])

        for i in range(start, len(S)):
            self.dfs(read_list + [S[i]], i + 1, S)

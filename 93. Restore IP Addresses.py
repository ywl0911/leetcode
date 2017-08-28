class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        parts = 0
        self.result = []
        ready = ''
        self.dfs(s, parts, ready)
        return (self.result)

    def dfs(self, s, parts, ready):
        if parts == 4:
            if s == '':
                self.result.append(ready[1:])
            return

        for i in range(1, 4):
            if len(s) >= i:

                if int(s[:i]) <= 255:
                    self.dfs(s[i:], parts + 1, ready + '.' + s[:i])
                if s[0] == '0':
                    break


s = Solution()
print(s.restoreIpAddresses(
    "121312211"))

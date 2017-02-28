class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
                :type s: str
                :rtype: int

                """
        if len(s)==0:
            return 0
        visted = {}
        start = 0
        maxlen = 1
        templen = 0
        for p in range(len(s)):
            if p == start:
                visted[s[p]] = p
                templen = 1
                continue

            if s[p] in s[start:p]:
                pass
                start = visted[s[p]] + 1
                templen = p - start+1
                visted[s[p]] = p
            else:
                templen += 1
                visted[s[p]] = p

            maxlen = max(maxlen, templen)

        return maxlen


a = Solution()
print a.lengthOfLongestSubstring("")

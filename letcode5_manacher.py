# Python
# -*- coding: utf-8 -*-
# Manacher算法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'

        Max_Right = 0
        pos = 0
        Max_length = 0
        RL = [0] * len(s)
        for i in range(len(s)):
            if i < Max_Right:
                RL[i] = min(Max_Right - i, RL[2 * pos - i])
            else:
                RL[i] = 0

            # 更新RL[i]
            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i + RL[i]] == s[i - RL[i]]:
                RL[i] += 1

            if i + RL[i] > Max_Right:
                Max_Right = i + RL[i] - 1
                pos = i

        ii = 0
        ii_index = 0
        for j_index,j in enumerate(RL):
            if j > ii:
                ii=j
                ii_index=j_index
        return str(s[ii_index-ii+1:ii_index+ii]).replace('#','')


s = Solution()
print s.longestPalindrome("aba")

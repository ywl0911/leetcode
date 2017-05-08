class Solution(object):
    @staticmethod
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 考虑第一种情况，一.*大头


        previos = ''
        index_s = 0
        for i in range(len(p)):
            if s[i] == p[i]:
                continue
            else:
                pass

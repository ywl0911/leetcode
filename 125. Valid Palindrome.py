class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        index = 0
        ss = []
        for i in range(len(s)):
            if ord('a') <= ord(s[i]) <= ord('z') or ord('0') <= ord(s[i]) <= ord('9'):
                ss.append(s[i])

        n = len(ss)
        if n <= 1:
            return True

        for i in range(n):
            if ss[i] != ss[n - i - 1]:
                return False
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

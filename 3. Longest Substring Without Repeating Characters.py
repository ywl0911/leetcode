class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
                :type s: str
                :rtype: int

                """
        if len(s)==0:
            return 0

        n=len(s)

        start=0
        end=1
        max_length=1
        while end<n:
            # print(s[end],s[start:end])
            if s[end] in s[start:end]:
                max_length=max(max_length,end-start)
                chongfu_index=s[start:end].index(s[end])+start
                start=chongfu_index+1
            else:
                end+=1

        max_length = max(max_length, end - start)

        return max_length

s=Solution()
print(s.lengthOfLongestSubstring('pwwkew'))
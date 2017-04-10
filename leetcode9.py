class Solution(object):
    @staticmethod
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        x_copy=x
        x_pa=0
        while x%10>0:
            x_pa=x_pa*10+x%10
            x=x-x%10
            print(x_pa)
        if x_pa==x_copy:
            return True
        else:
            return False

print(Solution.isPalindrome(1002))
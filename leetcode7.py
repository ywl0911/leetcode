class Solution(object):
    def reverse(self, x):
        if x<-2**31 or x>2**31:
            return 0
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:
            x=-x
            flag=-1

        x_str=list(str(x))
        x_str.reverse()
        a= int(''.join(x_str))*flag
        if a<-2**31 or a>2**31:
            return 0
        return a



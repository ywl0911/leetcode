class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        qian = num // 1000  # 板凳除,python2正好相反
        bai = (num // 100) % 10  # 板凳除
        shi = (num // 10) % 10  # 板凳除
        one = num % 10
        M = ['', 'M', 'MM', 'MMM']  # M=1000
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']  # C=100
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']  # X=10
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']  # I=1
        return M[qian] + C[bai] + X[shi] + I[one]


a = range(0, 2000, 2)
b = Solution()
for i in a:
    print(b.intToRoman(i))

class Solution(object):
    # 按照数字转罗马的方法转回去就行

    def romanToInt(self, s):
        """
        :type num: int
        :rtype: str
        """

        d = {'M': 1000, 'MM': 2000, 'MMM': 3000,
             'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
             'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
             'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
        sum = 0
        temp = ''
        for i in range(len(s)):
            if temp + s[i] in d.keys():
                temp += s[i]
                continue
            else:
                sum += d[temp]
                temp = s[i]
        sum += d[temp]

        return sum

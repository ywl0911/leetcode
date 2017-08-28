class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_len = len(a)
        b_len = len(b)
        if a_len > b_len:
            for i in range(a_len - b_len):
                b = '0' + b
        if b_len > a_len:
            for i in range(b_len - a_len):
                a = '0' + a

        result = []
        jinwei = 0
        for i in reversed(range(len(a))):
            he = int(a[i]) + int(b[i]) + jinwei

            temp_result = (he) % 2
            if he > 1:
                jinwei = he // 2
            else:
                jinwei = 0

            result.append(str(temp_result))

        if jinwei == 1:
            result.append('1')

        result = ''.join(result)
        result = result[::-1]
        return result



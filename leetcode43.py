class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = []
        result = []

        for i in range(len(num2) - 1, -1, -1):  # i为下面的乘数
            jinwei = 0
            temp_result = []
            for j in num1[::-1]:  # j为上面的乘数
                ji = int(num2[i]) * int(j) + jinwei
                jinwei = ji // 10
                gewei = ji % 10
                temp_result.insert(0, gewei)

            temp_result.insert(0, jinwei)
            result.append(temp_result)

        # print(result)
        # 补后面的0
        for i in range(1, len(num2)):
            for j in range(i):
                result[i].append(0)
        # print(result)

        # 补前面的0
        max_len = max([len(i) for i in result])
        for i in range(len(num2)):
            for j in range(max_len - len(result[i])):
                result[i].insert(0, 0)
        # print(result)

        last_result = []
        jinwei = 0
        for i in range(max_len - 1, -1, -1):  # i为列

            temp_sum = 0
            for j in range(len(num2)):
                temp_sum += result[j][i]

            temp_sum = temp_sum + jinwei

            gewei = temp_sum % 10
            jinwei = temp_sum // 10

            last_result.insert(0, str(gewei))

        while last_result[0]=='0' and len(last_result)>1:
            del last_result[0]


        return ''.join(last_result[i:])


s = Solution()
print(s.multiply('0', '0'))

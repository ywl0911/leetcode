class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])

        shang = 0
        xia = m - 1

        zuo = 0
        you = n - 1

        result = []
        while shang < xia and zuo < you:
            # 处理第一行
            for i in range(zuo, you):
                result.append(matrix[shang][i])
            # 处理右边一列
            for i in range(shang, xia):
                result.append(matrix[i][you])
            # 处理下边一行
            for i in range(you, zuo, -1):
                result.append(matrix[xia][i])
            # 处理左边一列
            for i in range(xia, shang, -1):
                result.append(matrix[i][zuo])

            zuo += 1
            you -= 1
            shang += 1
            xia -= 1

        if shang == xia:
            for i in range(zuo, you + 1):
                result.append(matrix[shang][i])
            return result
        if zuo == you:
            for i in range(shang, xia + 1):
                result.append(matrix[i][zuo])
            return result
        return result


s = Solution()
print(s.spiralOrder([[1, 2], [3, 4]]))

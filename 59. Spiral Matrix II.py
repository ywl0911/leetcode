class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]

        shang = zuo = 0
        xia = you = n - 1

        A = [[0 for i in range(n)] for j in range(n)]
        current = 1
        while zuo < you and shang < xia:
            for i in range(zuo, you):
                A[shang][i] = current
                current += 1
            for i in range(shang, xia):
                A[i][you] = current
                current += 1
            for i in range(you, zuo, -1):
                A[xia][i] = current
                current += 1
            for i in range(xia, shang, -1):
                A[i][zuo] = current
                current += 1

            shang += 1
            xia -= 1
            zuo += 1
            you -= 1

        if shang == xia:
            A[shang][zuo] = current

        return A

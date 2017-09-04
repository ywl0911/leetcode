class Solution(object):
    def search(self, L1, L2):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L1 = '0' + L1
        L2 = '0' + L2
        m = len(L1)
        n = len(L2)
        c = [[0 for i in range(n)] for j in range(m)]
        b = [[0 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):

                if L1[i] == L2[j]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    b[i][j] = 'xie'
                else:
                    c[i][j] = max(c[i - 1][j], c[i][j - 1])
                    if c[i - 1][j] > c[i][j - 1]:
                        b[i][j] = 'shang'
                    else:
                        b[i][j] = 'zuo'
        return b, c


def p(b, L1, L2, i, j):
    if i==0 or j==0:
        return
    if b[i][j] == 'xie':
        p(b, L1, L2, i - 1, j - 1)
        print L1[i]
    elif b[i][j] == 'zuo':
        p(b, L1, L2, i, j - 1)
    else:
        p(b, L1, L2, i - 1, j)


L1 = 'BDCABA'
L2 = 'ABCBDAB'
s = Solution()

b, c = s.search(L1, L2)
print b
print c
L1 = '0' + L1
L2 = '0' + L2
p(b, L1, L2, len(L1) - 1, len(L2) - 1)

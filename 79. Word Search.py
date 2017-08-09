class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        self.result = False
        point = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    point.append([i, j])
        print
        point
        self.dfs(board, word, point)
        return self.result

    def dfs(self, board, target, point):
        if target == '':
            self.result = True
            return
        if len(point) == 0:
            return

        for p in point:
            # print p[0],'>',p[1]
            if target[0] == board[p[0]][p[1]]:
                temp = board[p[0]][p[1]]
                board[p[0]][p[1]] = None
                adjacent = self.get_adjacent(p, board)
                t = target[1:]
                self.dfs(board, t, adjacent)
                board[p[0]][p[1]] = temp

    def get_adjacent(self, p, board):
        a = []
        if p[0] - 1 >= 0:
            a.append([p[0] - 1, p[1]])
        if p[0] + 1 < len(board):
            a.append([p[0] + 1, p[1]])
        if p[1] - 1 >= 0:
            a.append([p[0], p[1] - 1])
        if p[1] + 1 < len(board[0]):
            a.append([p[0], p[1] + 1])

        return a

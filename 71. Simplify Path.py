class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == '/':
            return path

        result = []
        path = path.split('/')

        for i in path:
            if i == '':
                continue
            if i == '.':
                continue
            if i == '..':
                if len(result) == 0:
                    continue
                result.pop()
                continue
            result.append(i)

        return '/' + '/'.join(result)

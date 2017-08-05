class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == []:
            return []

        from collections import defaultdict
        strs_new = []
        for i in strs:
            strs_new.append(''.join(sorted(i)))

        dic = defaultdict(list)
        for i in range(len(strs_new)):
            dic[strs_new[i]].append(strs[i])

        return list(dic.values())

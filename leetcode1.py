class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        odd = [i for i in nums if i % 2 == 1]
        even = [i for i in nums if i % 2 == 0]
        if target % 2 == 1:
            [odd_index, even_index] = \
                [[i_index, j_index] for i_index, i in enumerate(odd) for j_index, j in enumerate(even)
                 if
                 i + j == target][0]
            return sorted([list(nums).index(odd[odd_index]), list(nums).index(even[even_index])])
        if target % 2 == 0:
            a = [[i_index, j_index] for i_index in range(len(odd)) for j_index in
                 range(i_index + 1, len(odd)) if
                 odd[i_index] + odd[j_index] == target]
            if len(a) > 0:
                [odd_index_1, odd_index_2] = a[0]
                if odd[odd_index_1] == odd[odd_index_2]:
                    nn=list(nums)
                    b = nn.index(odd[odd_index_1])
                    nn.remove(odd[odd_index_1])
                    c = nn.index(odd[odd_index_1]) + 1
                    return [b, c]
                return sorted([list(nums).index(odd[odd_index_1]), list(nums).index(odd[odd_index_2])])

            [even_index_1, even_index_2] = [[i_index, j_index] for i_index in range(len(even)) for j_index in
                                            range(i_index + 1, len(even)) if
                                            even[i_index] + even[j_index] == target][0]
            if even[even_index_1] == even[even_index_2]:
                nn = list(nums)
                b = nn.index(even[even_index_1])
                nn.remove(even[even_index_1])
                c = nn.index(even[even_index_1]) + 1
                return [b, c]
            return sorted([list(nums).index(even[even_index_1]), list(nums).index(even[even_index_2])])


# s = Solution()
# print(s.twoSum(nums=[0,4,3,0], target=0))

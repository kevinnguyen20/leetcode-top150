class Solution: # not optimized, can be solved in linear time with O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        result = {}
        max = 0
        res = 0

        for n in nums:
            if n in result:
                result[n] += 1
            else:
                result[n] = 1

        for k in result:
            if result[k] > max:
                max = result[k]
                res = k

        return res

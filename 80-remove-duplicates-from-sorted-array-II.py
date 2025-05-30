class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        else:
            index = 0
            for n in nums:
                if index < 2 or n > nums[index-2]:
                    nums[index] = n
                    index += 1

        return index

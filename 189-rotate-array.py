class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res = []
        res = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            res[(i+k) % len(nums)] = nums[i]

        for k in range(len(nums)):
            nums[k] = res[k]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        for i in range(len(nums)):
            ls = nums[i+1:]
            if((target - nums[i]) in ls):
                index = ls.index(target-nums[i])
                ind = index + i + 1
                return [i, ind]

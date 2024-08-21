
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [None]*n
        output[0] = 1
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        # print(output)
        right = 1
        for x in range(n-1, -1, -1):
            output[x] *= right
            right *= nums[x]


        return output

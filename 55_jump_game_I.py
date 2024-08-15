#Difficulty: medium
#time: O(N)
# space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n==1):
            return True
        target = n-1
        for i in range(n-2, -1,-1):
            if nums[i]+i >= target:
                target=i
                if i == 0:
                    return True
                    
            else:
                if i == 0:
                    return False

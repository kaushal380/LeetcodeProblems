#difficulty:MEDIUM
#time: O(N)
#space: 0(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1):
            return 0
        target = n-1
        currentCapacity = nums[0]
        currentFurthest = nums[0]
        if(currentCapacity >= target):
            return 1
        jumps = 1
        for i in range(n-1):
            currentFurthest = max(currentFurthest, i+nums[i])
            if(i+nums[i] >= target):
                jumps+=1
                return jumps
            
            if(i>=currentCapacity):
                currentCapacity = currentFurthest
                jumps+=1

        

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if(n <= 1 or k == 0):
            return

        m = k%n
        if(m == 0):
            return
        lst = nums[:-1*m]
        # print(lst)
        nums[:-1*m] = []
        nums.extend(lst)
        

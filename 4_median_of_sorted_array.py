
# brute force method

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1+nums2
        lst.sort()
        print(lst)
        median = 0
        if(len(lst) % 2 == 0):
            median = (lst[len(lst)//2]+lst[(len(lst)//2) - 1]) / 2
        else:
            median = lst[len(lst)//2]
        return median

# optimized

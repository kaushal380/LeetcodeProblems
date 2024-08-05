# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        lst = []
        for i in range(len(arr)):
            lit = arr[:i]+arr[i+1:]
            if(arr[i] not in lit):
                lst.append(arr[i])
            if(len(lst) >= k):
                return arr[i]

        return ""


        

# difficulty: Medium
# topics: String, Hash map

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        maxLen = len(substr)
        for i in s:
            if(i not in substr):
                substr+=i
            else:
                ind = substr[::-1].index(i)
                ind = len(substr)-ind
                substr = substr[ind:] + i

            maxLen = max(maxLen, len(substr))

        return maxLen

        

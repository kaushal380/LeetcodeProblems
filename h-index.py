#medium

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        n = len(citations)

        if(n == 1 and citations[0]>=1):
            return 1

        print(citations)
        for i in range(n):
            if(citations[i] >= (n-i)):
                return n-i
            if(n-i) >= citations[i]:
                h = citations[i]
        return h
        

#Difficutly:medium
#topic: string
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        lst = []
        for x in range(numRows):
            lst.append([])
        print(lst)
        n = 0
        asc = True
        for i in s:
            lst[n].append(i)
            if(n == numRows-1):
                asc = False
            elif(n==0):
                asc = True
            if asc:
                n+=1
            else:
                n-=1
        strBulder = ""
        for m in lst:
            st = "".join(m)
            strBulder += st
        return strBulder




 

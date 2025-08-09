class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        d=+1
        cr=0
        rows =[""]* numRows
        if numRows == 1 or numRows >= len(s):
            return s
        for i in s:
            rows[cr]+=i
            cr+=d

            if cr==numRows-1 or cr==0:
                d*=-1
        return "".join(rows)
            
            
            


            
            


        
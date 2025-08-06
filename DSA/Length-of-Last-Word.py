class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        n=len(s)-1
        while n >= 0 and s[n] == " ":
            n -= 1
        
        for i in range(n,-1,-1):
            if s[i]!=" ":
                count+=1
            else:
                break
                
        return count
        
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()

        s = re.sub(r'[^a-zA-Z0-9]', '', s)


        i=0
        j=len(s)-1
        while i < len(s)//2:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        
        return True




        
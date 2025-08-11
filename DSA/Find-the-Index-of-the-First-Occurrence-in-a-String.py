class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            word=haystack[i:i+m]
            if word == needle:
                return i
        return -1
            

        
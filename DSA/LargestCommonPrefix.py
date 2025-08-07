class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_len = min(len(word) for word in strs)
        for i in range(min_len):
            char=strs[0][i]
            for word in strs[1:]:
                if word[i] != char:
                    return strs[0][:i] 
        return strs[0][:min_len]


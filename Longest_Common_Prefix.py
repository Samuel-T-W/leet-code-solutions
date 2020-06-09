class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs)==0):
            return ""
        s = strs[0]
        strs.pop(0)
        for i in strs:
            while(not i.startswith(s)):
                s=s[:-1]
        return s
            
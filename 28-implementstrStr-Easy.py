"""
Faster than 99.41 for first submission
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        needleSet = {needle}
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] in needleSet:
                    return i
        return -1

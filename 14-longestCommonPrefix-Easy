class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        string = strs[0]
        while True:
            for index,item in enumerate(strs):
                success = False
                try:
                    if item.index(string) != 0:
                        break
                except ValueError:
                        break
                success = True
            if success == True:
                return string
            string = string[:-1]
            if len(string) == 0:
                return ""

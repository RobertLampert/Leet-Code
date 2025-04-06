class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        stringLength = len(strs[0])
        for i in range(stringLength):
            char = strs[0][i]
            for index in strs:
                if i < len(index) and index[i] == char:
                    continue
                else:
                    return prefix
            prefix += char
        return prefix

solution = Solution()
stringArr = ["","",""]
print(solution.longestCommonPrefix(stringArr))
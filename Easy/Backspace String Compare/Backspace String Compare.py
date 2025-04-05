class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stackFirst = []
        stackSecond = []
        for char in s:
            if char == "#":
                if len(stackFirst) > 0:
                    stackFirst.pop()
                else:
                    continue
            else:
                stackFirst.append(char)
        for char in t:
            if char == "#":
                if len(stackSecond) > 0:
                    stackSecond.pop()
                else:
                    continue
            else:
                stackSecond.append(char)

        return stackFirst == stackSecond

solution = Solution()
firstString = "a##c"
secondString = "#a#c"
print(solution.backspaceCompare(firstString,secondString))

# f

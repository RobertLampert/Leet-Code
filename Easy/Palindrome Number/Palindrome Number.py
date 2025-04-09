class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        reversedString = ""
        for char in x:
            reversedString = char + reversedString
        return reversedString == x
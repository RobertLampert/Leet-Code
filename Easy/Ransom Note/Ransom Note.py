class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freqDict = {}
        for char in ransomNote:
            if char not in freqDict.keys():
                freqDict.update({char:ransomNote.count(char)})
        for key in freqDict:
            if magazine.count(key) < freqDict.get(key):
                return False
        return True
    

solution = Solution()
note = "test"
mag = "tesagain"

print(solution.canConstruct(note,mag))
        
class Solution(object):
    def isAnagram(self,s,t):
        dict_firstString = {}
        dict_secondString = {}
        for x in range(len(s)):
            if(s[x] in dict_firstString):
                dict_firstString[s[x]] +=1;
            else:
                dict_firstString[s[x]] = 1;
        for x in range(len(t)):
            if(t[x] in dict_secondString):
                dict_secondString[t[x]] +=1;
            else:
                dict_secondString[t[x]] = 1;
        if(dict_firstString == dict_secondString):
            return True;
        else:
            return False;

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  
print(solution.isAnagram("rat", "car"))  


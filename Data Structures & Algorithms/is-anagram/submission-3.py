class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        charArr = [0] * 26
        a = ord('a')
        for i in range(len(s)):
            charArr[ord(s[i])-a] = charArr[ord(s[i])-a]+1
            charArr[ord(t[i])-a] = charArr[ord(t[i])-a]-1
        for r in charArr:
            if r!=0:
                return False
        return True

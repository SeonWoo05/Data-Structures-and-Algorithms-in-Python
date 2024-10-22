# Leetcode 205
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        stot = {}
        ttos = {}

        for i in range(len(s)):
            schar = s[i]
            tchar = t[i]

            if schar in stot:
                if stot[schar] != tchar:
                    return False

            else:
                stot[schar] = tchar

            if tchar in ttos:
                if ttos[tchar] != schar:
                    return False
            
            else:
                ttos[tchar] = schar
        
        return True
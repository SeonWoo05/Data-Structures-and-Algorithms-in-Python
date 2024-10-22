# Leetcode 290
class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split() # 문자열을 공백기준으로 분리하여 리스트로 반환

        if len(pattern) != len(words):
            return False
        
        pdic = {}
        wdic = {}

        for i in range(len(pattern)):
            pchar = pattern[i]
            wchar = words[i]

            if pchar in pdic:
                if pdic[pchar] != wchar:
                    return False
            else:
                pdic[pchar] = wchar

            if wchar in wdic:
                if wdic[wchar] != pchar:
                    return False
                
            else:
                wdic[wchar] = pchar

        return True
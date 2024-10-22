# Leetcode 242
class Solution(object):
    def isAnagram(self, s, t):
        sdic = {}
        tdic = {}
        
        for i in s:
            if i in sdic:
                sdic[i] += 1
            else:
                sdic[i] = 1

        for i in t:
            if i in tdic:
                tdic[i] += 1
            else:
                tdic[i] = 1

        return sdic == tdic
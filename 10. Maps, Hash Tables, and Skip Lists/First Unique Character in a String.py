# LeetCode 387

class Solution(object):
    def firstUniqChar(self, s):
        ht = {}

        for val in s:
            if val in ht:
                ht[val] += 1
            else:
                ht[val] = 1

        for idx,val in enumerate(s):
            if ht[val] == 1:
                return idx

        return -1    
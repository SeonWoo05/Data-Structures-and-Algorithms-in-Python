# Leetcode 1047
class Solution(object):
    def removeDuplicates(self, s):
        stack = []

        for i in s:
            if stack and stack[-1] == i: # 원소가 존재하고 같아야 없앰
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)
from collections import deque

class Solution(object):
    def isValid(self, s):
        dq = deque()
        mapping = {')':'(', ']':'[', '}':'{'}
        
        for i in s:
            if i in ['(','[',"{"]:
                dq.append(i)
            else:
                if not dq or dq.pop() != mapping[i]: # not dq : 시퀀스 자료구조가 비었는지 확인
                    return False

        return len(dq) == 0
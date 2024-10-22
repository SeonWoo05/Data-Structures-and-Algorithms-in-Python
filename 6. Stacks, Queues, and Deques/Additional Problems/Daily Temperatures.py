# Leetcode 739
from collections import deque

class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures) # 더 따듯한 날이 없으면 0 => 처음부터 0으로 만들고 변경
        dq = deque()

        for idx,temp in enumerate(temperatures):
            while dq and temperatures[dq[-1]] < temp: # dq에 인덱스를 담아서
                # 이전 인덱스의 온도보다 현재의 온도가 높으면 그 인덱스 차이를 저장
                prev_idx = dq.pop()
                ans[prev_idx] = idx - prev_idx
            dq.append(idx)
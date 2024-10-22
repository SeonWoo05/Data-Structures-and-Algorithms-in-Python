# Leetcode 560
class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = []
        tmp_sum = 0
        
        for num in nums:
            tmp_sum += num
            prefix_sum.append(tmp_sum)

        table = {}
        count = 0
        table[0] = [1]
        for idx, prefix_sum in enumerate(prefix_sum):
            target = prefix_sum - k
            if target in table:
                count += len(table[target])
            if prefix_sum not in table:
                table[prefix_sum] = [idx]
            else:
                table[prefix_sum].append(idx) # 부분합이 같은 인덱스를 리스트에 추가하는 방식
        
        return count
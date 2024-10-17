# LeetCode 167

# (1) Hash Table
# numbers 의 idx 와 val을 각각 hashtable의 value와 key로 사용 (key를 통한 탐색이 쉽기때문)
class Solution(object):
    def twoSum(self, numbers, target):
        ht = {}

        for idx,val in enumerate(numbers):
            match_num = target - val
            match_idx = ht.get(match_num)

            if match_idx is not None:
                return [match_idx + 1, idx + 1]
            
            ht[val] = idx


# (2) Two Pointers
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left + 1, right + 1]
            
            elif curr_sum < target:
                left += 1
            
            else:
                right -= 1
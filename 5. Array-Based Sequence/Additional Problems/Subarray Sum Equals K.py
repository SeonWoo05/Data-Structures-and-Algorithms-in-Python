# Leetcode 560
class Solution(object):
    def subarraySum(self, nums, k):
        sum_counts = {0: 1}  # 첫 번째 원소부터 시작하는 부분 배열에서 바로 합이 k가 되는 경우를 처리하기 위해 설정
        curr_sum = 0  # 현재까지의 누적합
        cnt = 0  # 부분 배열의 개수
        
        for num in nums:
            curr_sum += num  # 현재 값을 더해 누적합을 구함
            
            # 현재 누적합에서 k를 뺀 값이 해시맵에 있으면, 그 수만큼 부분 배열이 존재함
            if (curr_sum - k) in sum_counts:
                cnt += sum_counts[curr_sum - k]
            
            # 현재 누적합을 해시맵에 저장하여 이후 부분 배열 계산에 사용
            sum_counts[curr_sum] = sum_counts.get(curr_sum, 0) + 1
                # sum_counts에서 curr_sum이라는 키를 찾아 curr_sum이 등장한 횟수를 가져옴
                # 두번째 인자는 curr_sum이라는 키가 없으면 0을 반환
        
        return cnt                
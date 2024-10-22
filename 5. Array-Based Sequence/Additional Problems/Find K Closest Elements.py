# Leetcode 658
class Solution:
    def findClosestElements(self, arr, k, x):
        # 이진 탐색으로 x와 가장 가까운 위치 찾기
        left, right = 0, len(arr) - 1
        
        # 이진 탐색: x에 가장 가까운 값을 찾는 과정
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        
        # 이진 탐색이 끝난 후, left와 right는 같은 값으로 설정됨
        # 그 위치는 x와 가장 가까운 값이거나 그 근처의 값
        left = right = left - 1  # left와 right를 모두 이 위치로 설정
        
        # 슬라이딩 윈도우: left와 right 포인터를 양쪽으로 확장해가며 k개의 가장 가까운 값 찾기
        while right - left - 1 < k:
            # 왼쪽으로 더 이상 갈 수 없으면 오른쪽으로만 확장
            if left == -1:
                right += 1
            # 오른쪽으로 더 이상 갈 수 없으면 왼쪽으로만 확장
            elif right == len(arr):
                left -= 1
            # 왼쪽 값이 더 가까운 경우 왼쪽으로 확장
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            # 오른쪽 값이 더 가까운 경우 오른쪽으로 확장
            else:
                right += 1
        
        # 결과적으로 left + 1에서 right까지가 가장 가까운 k개의 값
        return arr[left + 1:right]
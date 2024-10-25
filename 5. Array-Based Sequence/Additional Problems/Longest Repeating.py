# Leetcode 424
class Solution(object):
    def characterReplacement(s, k):
        count = [0] * 26  # 알파벳 빈도수를 기록하는 리스트
        max_count = 0  # 윈도우 내에서 가장 많이 등장하는 문자의 빈도
        start = 0  # 슬라이딩 윈도우의 시작 인덱스
        max_length = 0  # 최종 결과로 반환할 최대 길이

        for end in range(len(s)):
            # 현재 문자의 빈도 증가
            count[ord(s[end]) - ord('A')] += 1
        
            # 현재 윈도우에서 가장 많이 등장한 문자의 빈도 갱신
            max_count = max(max_count, count[ord(s[end]) - ord('A')])
        
            # 교체해야 할 문자의 개수 확인
            if (end - start + 1) - max_count > k:
                # 교체할 수 있는 문자의 개수가 k보다 많으면 start를 오른쪽으로 이동
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
        
            # 최대 길이 갱신
            max_length = max(max_length, end - start + 1)
    
        return max_length
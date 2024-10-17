# LeetCode 347

class Solution(object):
    def topKFrequent(self, nums, k):
        ht = {}

        for i in nums:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1

        # dictionary : sort 하는 함수 X => list
        # .items로 반환된 tuple들을 value로 하는 list 생성
        # sorted : 오름차순으로 정렬하지만, key라는 매개변수를 사용하면 정렬 기준을 지정가능
        # x는 tuple을 의미하고, x[1]은 value / value를 기준으로 내림차순 정렬
        sorted_items = sorted(ht.items(), key = lambda x: x[1], reverse=True)

        result = [item[0] for item in sorted_items[:k]]

        return result
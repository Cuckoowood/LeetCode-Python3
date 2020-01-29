"""
ͨ��Ƶ�����ж��Ƿ���Ի���
"""
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        # d��¼�������ֳ���Ƶ��
        d = Counter(nums)
        if len(nums) % k:
            return False
        for i in sorted(nums):
            if d[i] <= 0:
                continue
            for j in range(k):
                if i+j not in d or d[i+j] <= 0:
                    return False
                d[i+j] -= 1
        return True
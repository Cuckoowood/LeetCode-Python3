from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # ���ÿ�����������������̾���
        res = []
        # ����
        houses.sort()
        heaters.sort()
        for c in houses:
            # ���ֲ��ң���heaters��Ѱ���뷿�� c ����ļ�����
            left = 0
            right = len(heaters) - 1
            while left < right:
                mid = (left + right) >> 1
                if heaters[mid] < c:
                    left = mid + 1
                else:
                    right = mid
            # ���ҵ���ֵ���� c ����˵�� c ���ݴ�����һ����������c ���ݵ�����������̾���Ϊ 0
            if heaters[left] == c:
                res.append(0)
            # ���ü�����������ֵС�� c ��˵���ü������������� c ֮��û�б�ļ�����
            elif heaters[left] < c:
                res.append(c - heaters[left])
            # ���ü�����������ֵ���� c ����left������ 0 ��˵�� c ����left��left-1֮�䣬
            # ���ݵ�����������̾������left��left - 1���������� c ��ֵ����Сֵ
            elif left:
                res.append(min(heaters[left] - c, c - heaters[left - 1]))
            else:
                res.append(heaters[left] - c)
        return max(res)



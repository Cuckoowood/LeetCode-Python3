class Solution:
    def triangleNumber(self, nums: 'List[int]') -> 'int':
        nums.sort()
        res = 0
        # �Ӵ�С����
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i -1
            while l < r:
                # ֻҪ��С������ֵ֮�ʹ�������ֵ����һ�������������
                if nums[l] + nums[r] > nums[i]:
                    #i, r �ʹ�l��r-1������������Σ�����Ϊ (r-1) - l + 1 = r - l
                    res += (r-1) - l + 1
                    r -= 1
                else: l += 1
        return res
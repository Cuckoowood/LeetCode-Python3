class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        �򵥶���
        ʱ�临�Ӷ�: nums.length*log(max(nums)) = 17*5*10^4
        :param nums:
        :param threshold:
        :return:
        """
        L, R = 1, max(nums)
        while (L < R):
            mid = (L + R) >> 1
            # С�ڵ�����ֵ, ˵�� �𰸲�����mid����߾���mid
            if(sum(math.ceil(x/mid) for x in nums) <= threshold):
                R = mid
            # ������ֵ, ����mid�ұ�
            else:
                L = mid + 1
        return R
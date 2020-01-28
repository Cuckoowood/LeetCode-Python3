class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # �� A ������������������ͬ��ͬ����ô��ֵ���� A[-1]-A[0] ��
        #��Ӱ�������ɽ� A ��Ϊ������ A1<A2��Ϊ��ʹ��ֵ��С��ֻ�� A1 ͬ�ӣ� A2 ͬ������ô���� A �����ֵֻ���� A1 β�� A2 β����Сֵֻ���� A1 ͷ�� A2 ͷ���Ƚ���4��ֵ�Ϳ�����ò�ֵ��

        l = len(A)
        if l < 2:return 0
        A.sort()
        res = A[l-1]-A[0]
        for i in range(1,l):
            minu = min(A[0] + K, A[i] - K)
            maxu = max(A[i-1] + K, A[l-1] - K)
            res = min(res, maxu - minu)
        return res
class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # �Ӻ���ǰ�ҵ�һ��ǰ>�������λ�ã���Ϊtmp
        tmp = -1
        for i in range(len(A)-1, 0, -1):
            if A[i-1] > A[i]:
                tmp = i-1
                break
        
        # ���tmpΪ1��������Ϊ��������
        if tmp == -1:
            return A
        
        # ��tmp�ұ�Ѱ�ҵ�һ�����ֵ���ӽ�tmp�����ֵ�λ��
        index = tmp
        mindiff = float("inf")
        for j in range(tmp+1, len(A)):
            if A[j] < A[tmp]:
                diff = A[tmp] - A[j]
                if mindiff > diff:
                    mindiff = diff
                    index = j
        
        A[tmp], A[index] = A[index], A[tmp]
        return A
        
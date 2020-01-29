class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0 for i in range(len(A) + 1)] #s����ǰ׺�ͣ���s[i]��ʾsum(A[:i])
        kcnt = [0 for i in range(K)] #kcnt[i]����s���ж��ٸ�Ԫ�� mod K Ϊi
        for i in range(len(A)):
            s[i + 1] = s[i] + A[i]
        for item in s:
            kcnt[item % K] += 1
        #print s, kcnt

        return sum(x * (x - 1) // 2 for x in kcnt)
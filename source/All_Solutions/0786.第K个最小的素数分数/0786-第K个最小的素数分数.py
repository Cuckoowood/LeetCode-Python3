class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        l, r = 0, 1  # ��������Ͻ���½�
        lenA = len(A)
        while l < r:
            m = (l + r) / 2
            count = 0
            i = lenA - 1
            cur = [A[0]/A[-1], A[0], A[-1]]
            for j in reversed(range(1, lenA)):
                while i > -1 and A[i]/A[j] > m:  # �������в�����m�Ľ�����м���
                    i -= 1
                if i < 0:
                    break
                count += i + 1
                if A[i]/A[j] > cur[0]:  # ��¼�������㲻����m���������ֵ
                    cur = [A[i]/A[j], A[i], A[j]]
            if count == K:
                return cur[1:]
            if count < K:
                l = m
            else:
                r = m
'''
��������
[1,2,3,5]
3
[1,7]
1
[1,7,23,29,47]
8
https://leetcode-cn.com/submissions/detail/13488395/testcase/
https://leetcode-cn.com/submissions/detail/13490941/testcase/
https://leetcode-cn.com/submissions/detail/13491767/testcase/
'''
class Solution:
# ˼·��dp
# a,b�ֱ��¼ǰi�����ֵ
# ����λ��i, ���ֵ=ǰL��+b[i-L] ���� ǰM��]+a[i-M] ����ǰi-1λ�õ����ֵ
# res = max(res, A[i] - A[i - L] + b[i - L], A[i] - A[i - M] + a[i - M])

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        a, b = [0] * n, [0] * n  # a��L,b��M
        res = 0
        for i in range(1, n):
            A[i] += A[i - 1]
        for i in range(n):
            a[i] = A[i] if i < L else max(a[i - 1], A[i] - A[i - L])
            b[i] = A[i] if i < M else max(b[i - 1], A[i] - A[i - M])
            res = A[i] if i < L + M else max(res, A[i] - A[i - L] + b[i - L], A[i] - A[i - M] + a[i - M])
        return res

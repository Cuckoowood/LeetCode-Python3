from random import randint

class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.s = N - len(blacklist)
        # С��s�ĺ�����Ԫ�ؼ���
        b_lt_s = {i for i in blacklist if i < self.s}
        # ����s�ķǺ�����Ԫ�ؼ���
        # �ȼ��ڣ�w_gt_s = {i for i in range(self.s, N)} - set(blacklist)����л����
        w_gt_s = {*range(self.s, N)} - set(blacklist)
        # ��ӳ�䣬ʹ��zip����һ��
        # �ȼ��ڣ�self.m = {k: v for k,v in zip(b_lt_s, w_gt_s)}
        self.m = dict(zip(b_lt_s, w_gt_s))

    def pick(self):
        """
        :rtype: int
        """
        r = randint(0, self.s-1)
        return r if r not in self.m else self.m[r]
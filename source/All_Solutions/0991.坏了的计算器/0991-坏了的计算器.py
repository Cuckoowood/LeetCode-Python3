class Solution(object):
    # ˼·����Ҫ�м����������һ��YС��X,��ô��������£�ֻ�ܽ��з��ݼ���������Ҫ����X-Y�β���
    # �ڶ���Y>X����ô���ȹ۲죬Y�Ƿ�Ϊ�������������������ôֻ��Y��+1�������ż������ô�Ϳ���ֱ��Y��2���鿴�ǹ����
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        # �ݹ�˼·
        # if X == Y:
        #     return 0
        # if X > Y:
        #     return X - Y
        # if Y % 2 == 0:
        #     return 1 + self.brokenCalc(X,int(Y/2))
        # else:
        #     return 1 + self.brokenCalc(X,Y+1)
        # ѭ��˼·
        allnum = 0
        while X != Y:
            if X > Y:
                allnum += (X - Y)
                break
            if Y % 2 == 0:
                Y /= 2
                allnum+=1
            else:
                Y += 1
                allnum+=1
        return int(allnum)
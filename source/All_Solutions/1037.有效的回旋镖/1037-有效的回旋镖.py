class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        #�������������ͬ
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        x0, x1, x2 = points[0][0], points[1][0], points[2][0]
        y0, y1, y2 = points[0][1], points[1][1], points[2][1]
        
        #���ǳ�������Ϊ0
        if x0 == x1 or x2 == x1:
            return x0 != x2
        
        
        #���ǲ��������㹲�ߵ����
        return abs (1.0 * (y2 - y1) / (x2 - x1) - 1.0*(y1 - y0) /(x1 - x0)) > 0.0001
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dis = []
        p = [p1, p2, p3, p4]

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                tmp = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                dis.append(tmp)
        # ��������Σ���ô��������ֻ�������������Ҫô��4���� Ҫô��2���Խ���  ��������֮����ôǰ�ĸ������Ǳ߳�  �����������ǶԽ���
        # ���ֻУ��߳�����ô����������   ������Ҫ�ж�һ�¶Խ��߳����Ƿ����
        dis.sort()
        return True if dis[0] > 0 and dis[0] == dis[3] and dis[4] == dis[5] else False

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # ˼·: ���ڵ�ǰ��ĳһ����԰���޳��������ڽӻ�԰�Ļ������࣬��ʣ�µ�������ѡһ�ּ��ɡ�
        # 1. �����ڽӾ���G; 2. ��res�б��浱ǰ��԰��������
        res = [0]*N
        G = [[] for _ in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            # ���ڵ�ǰ��԰, �ų����ڽӵĻ�԰�Ļ��־�ok�ˣ�Ȼ��pop��һ��
            res[i] = ({1,2,3,4} - {res[j] for j in G[i]}).pop()
        return res
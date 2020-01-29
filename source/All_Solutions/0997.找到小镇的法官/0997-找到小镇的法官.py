class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        a = [0 for x in range(N+1)] #���������
        b = [0 for x in range(N+1)] #�����ŵ���

        for num in trust:
            a[num[1]] += 1   #�洢��Ϊ����������
            b[num[0]] += 1

        for i,num in enumerate(a):
            if(i!=0 and num == N-1): #�����˶����ŷ���
                if(b[i] == 0): #���ٲ������κ���
                    return i
        return -1
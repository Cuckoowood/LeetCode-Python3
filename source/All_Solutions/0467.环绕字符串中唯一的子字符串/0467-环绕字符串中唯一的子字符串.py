class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p: return 0
        N = len(p)
        arr = [0] * 128 #����ǰ��������ִ��ĳ��ȵ�����
        arr[ord(p[0])] = 1#��ʼ����һ����ĸ����Ϊ1
        prelen = 1#����ǰ�ó��ȵ���ʱ����
        for i in range(1, N):
            m = ord(p[i]) - ord(p[i-1])
            if m == 1 or m == -25:#ǰ����ĸ����
                prelen += 1  #�������1
            else:
                prelen = 1 #����������Ϊ1
            arr[ord(p[i])] = max(prelen, arr[ord(p[i])])
        return sum(arr)


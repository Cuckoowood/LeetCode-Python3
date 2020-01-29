class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        cnt = 0 #ͳ�Ʊ�����ȫ��26���ַ���Ƶ����ͬ�ĸ�������cnt==s1��ĸ�ĸ�����ʱ�򣬾���ȫ���������⣬������
        p = q = 0 #��������[p,q]
        while q < l2:
            c2[s2[q]] += 1
            if c1[s2[q]] == c2[s2[q]]: #���ڱ���������ĸ��������ִ�����ͬ
                cnt += 1               #ͳ�Ʊ���+1
            if cnt == len(c1):         #�жϽ��д��ǰ�棬��ʱ֤��s2�������ں�s1ȫ���ַ���ͬ��������
                return True
            q += 1                     #������������
            if q - p + 1 > l1:         #���ǹ����һ���������ڵ������жϣ�����������ά���߽绬������
                if c1[s2[p]] == c2[s2[p]]:    #�ж��Ե�ifд��ǰ�棬��Ϊһ��Ƶ�ʱ仯�����ͳ�Ʊ����ͼ�1
                    cnt -= 1
                c2[s2[p]] -= 1                #�ֵ��ϣ���Ƴ���ǰ����ַ�
                if c2[s2[p]] == 0:            #����counter���ԣ����valueΪ0������ɾ����
                    del c2[s2[p]]
                p += 1                        #��ǰ����±����ƶ�
        return False

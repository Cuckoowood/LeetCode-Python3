class Solution(object):
    def minSwapsCouples(self, row):
        """
        ÿ������λ��һ�ԣ��ٶ���ߵ��˶��ǺϷ��Ĳ��䣬���TA�ұߵ�����TAƥ����
        ��������ƥ�����ҵ�TA��ƥ��������TA�ұߵ��˽�����
        """
        def find_another(n):
            if n % 2 == 0:
                return n + 1
            else:
                return n - 1

        c = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = find_another(p1)
            if row[i+1] != p2:
                j = row.index(p2)
                row[i+1], row[j] = row[j], row[i+1]
                c += 1

        return c
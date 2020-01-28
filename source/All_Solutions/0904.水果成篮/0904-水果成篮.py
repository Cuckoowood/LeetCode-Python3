class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # ����˼·��ά��һ����ǰ���ڴ���Ĺ���������ts����󳤶�Ϊ2
        # �������������� [1,2,2,3]
        # ��ʼ��ʱ��ts = []������ǰ��� 1 �� 2ʱ��ֱ�Ӱ� 1 �� 2 �ŵ�ts���Ϊ ts Ŀǰ�ǿյģ�ͬʱ cur_len + 1
        # �����ڶ��� 2������ 2 �� ts ���棬����Ŀǰ��Ȼû�г��ֵ�������𣬲�������cur_len + 1
        # ���� 3 ʱ�������˵�������𣬴�ʱ��Ҫ����һ�Σ������ cur_len > max_len�� �� cur_len ���� max_len
        # Ȼ�����һ�� ts����ʱ ts Ӧ�� = [2, 3]
        # ����һЩϸ����Ҫ����������Բο�����
        p1 = None
        p2 = None
        cur_len = None
        max_len = None
        ts = []
        for i, t in enumerate(tree):
            # �ж��Ƿ������˵��������
            if t in ts:
                cur_len += 1
                if t == ts[0]:
                    p1 = p2
                    p2 = i
                    ts = ts[::-1]
                
            else:
                if len(ts) == 0:
                    ts.append(t)
                    p1 = i
                    cur_len = 1
                elif len(ts) == 1:
                    ts.append(t)
                    p2 = i
                    cur_len += 1                
                else:
                    # ��ʱ�����˵�������𣬽���һ��
                    if max_len is None or cur_len > max_len:
                        #print(p1, p2, i, cur_len)
                        max_len = cur_len
                    cur_len = i - p2 + 1
                    p1 = p2
                    p2 = i
                    ts = [ts[1], t]
                    
        if max_len is None or cur_len > max_len:
            max_len = cur_len
        return max_len
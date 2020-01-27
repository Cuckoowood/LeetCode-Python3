class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        # �ù�ϣ�ֵ� charPos ��¼ ring ��ÿ���ַ����ֵ�����λ�ã��ӿ����
        charPos = {}
        for i, char in enumerate(ring):
            if char not in charPos:
                charPos[char] = []
            charPos[char].append(i)
        
        n = len(ring)
        
        # last��curr �д�Ŷ�Ԫ�飺
        #       ������ָ�봦�ڵ�λ�ã������λ����Ҫ�����ٲ�����
        # last ��ʾ��һ���ҵ��ַ������
        # curr ��ʾ��ǰ�ַ��������ÿһ�ֽ������
        # last ��ʼ��Ϊһ��Ԫ��(0, 0)����ʾ�ʼ���̴���λ�� 0���Ѿ�����0 ��
        last = [(0, 0)]
        curr = []
        
        for char in key:                    # ��ǰҪ�ҵ��ַ�
            for currPos in charPos[char]:   # Ҫָ����ַ���ָ��Ӧ�õ��������λ��
                leastStep = last[0][1] + n  # �����λ���������ٲ�������ʼ��Ϊһ���ϴ��ֵ
                for (lastPos, lastStep) in last:    # �ϸ��ַ����п���λ�ã�������Ӧ�ۻ������ٲ���
                    # ���ϸ��ַ���λ�ã����ﵱǰλ�ã���������ٲ���
                    leastStep = min(lastStep + min((currPos + n - lastPos) % n, (lastPos + n - currPos) % n) + 1, leastStep)
                # �ҵ����ﵱǰλ�õ����ٲ������ѣ�λ�ã����������� curr
                curr.append((currPos, leastStep))
            
            # ��� curr �󣬹��� last �� curr ��������
            last, curr = curr, last
            curr.clear()
        
        # �������ٲ���
        return min(list(map(lambda x: x[1], last)))


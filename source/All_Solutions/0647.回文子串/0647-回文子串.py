class Solution:
    def countSubstrings(self, s: str) -> int:
        # �Ȱ��ַ���ת����(�ַ�,����)���б���ʽ����'aabccc'��Ϊ[('a',2),('b',1),('c',3)]���������ټ���
        counts, count = [], 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                counts.append((s[i], count))
                count = 1
        counts.append((s[-1], count))
        res = 0
        for i in range(len(counts)):
            res += counts[i][1]*(counts[i][1]+1)//2
            # ����(�ַ�,����)�ܹ��ɵĻ��Ĵ��������������֪ʶ������x����ĸ���ɵ�x+1������ѡ���������ȡ�Ӵ�
            # �������C_(x+1)^2�������Ϊ3���򹹳�(3+1)*3/2=6��
            j = 1  # ��counts[i]Ϊ���Ĵ��������߿��ǵ�����(�ַ�������������
            while i-j >= 0 and i+j < len(counts):
                left, right = counts[i-j], counts[i+j]
                if left[0] == right[0]:  # �����ַ���ͬ
                    if left[1] != right[1]:  # ������ͬ
                        res += min(left[1], right[1])  # ������Сֵ
                        break  # ֹͣ����
                    else:
                        res += left[1]  # ���Ҽ�����ͬ����ֱ�Ӽ��������
                        j += 1  # ��������
                else:
                    break  # �ַ���ֱͬ��ֹͣ����
        return res


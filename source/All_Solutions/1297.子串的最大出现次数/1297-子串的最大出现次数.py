"""
�������ڣ����ڴ�СΪminSize����ΪҪ����ֵĴ���������maxSize���Ӵ�����������ôminSize��ȻҲ�����,���Ҵ�����Ȼ���ڵ���maxSize�Ĵ���
"""
from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = []
        # �Ȱѷ���������ȫ���Ѽ�����
        for i in range(0, len(s)-minSize+1):
            ts = s[i:i+minSize]
            if len(set(ts)) > maxLetters:
                continue
            else:
                res.append(ts)
        if not res:
            return 0
        # ���س��ִ�������
        return sorted(Counter(res).items(), key=lambda x:x[1], reverse=True)[0][1]
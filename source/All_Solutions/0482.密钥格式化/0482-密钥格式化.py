class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # ����˼ά��������Ŀ�е�һ����������������һ�飬�ǲ��Ǻ�����������������������ƴ��-
        # ���Ա��⽫�ַ�����תһ�£�Ȼ��ÿ�λ���ǰ��ͺ���
        s = S.upper().replace('-','')[::-1]
        res = ''
        for i in range(len(s)):
            if i%K == 0 and i!=0: res = '-' + res
            res = s[i] + res
        return res

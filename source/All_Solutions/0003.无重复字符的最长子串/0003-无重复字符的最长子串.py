class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ��һ�о����û�������
        # ά��һ����������
        # ���Ǳ߽�����
        if not s: return 0

        hashmap = {s[0]:0}
        start = 0
        res = 1
        for i in range(1, len(s)):
            if s[i] not in s[start:i]:
                hashmap[s[i]] = i
                res = max(res,i - start + 1)
            else:
                start = hashmap[s[i]] + 1
                hashmap[s[i]] = i
        return res
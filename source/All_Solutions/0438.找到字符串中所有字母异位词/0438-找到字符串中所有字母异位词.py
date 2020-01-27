class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # ��������ģ������������
        # ord("a") = 97
        sArr = [ord(i)-97 for i in s]
        pArr = [ord(i)-97 for i in p]
        hash = [0 for i in range(26)]
        m,n  = len(s),len(p)
        # ����hashӳ������
        for i in range(n):
            hash[pArr[i]] += 1
        l,r,count,res= 0,0,0,[]
        while r < m:
            hash[sArr[r]] -= 1
            if hash[sArr[r]] >= 0: 
                count += 1
            # �ƶ���ָ��
            if r > n - 1:
                hash[sArr[l]] += 1
                if hash[sArr[l]] > 0: 
                    count -= 1
                l += 1
            if count == n:
                res.append(l)
            r += 1            
        return res


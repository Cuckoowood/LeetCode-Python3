class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = list()
        l = len(S)
        if l == 0:
            return [""]
            
        def dfs(start, temp):
            if start >= l or len(temp) == l: #�Ѿ��ҵ���һ����
                res.append(temp)
                return
            # print start, temp
            if S[start].isdigit(): #���־�ֱ�Ӽ�
                dfs(start + 1, temp + S[start])
            
            elif S[start].islower(): #��ĸ�ͼӱ���Ͷ�����
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].upper())

            elif S[start].isupper():
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].lower())
        
        dfs(0, "")
        return res
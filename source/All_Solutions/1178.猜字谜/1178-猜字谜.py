class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        for i in range(len(words)):
            words[i] = "".join(sorted(set(words[i])))
        record = Counter(words) #ͳ��ÿ����ϳ��ֵ�Ƶ��
        
        res = []
        for p in puzzles:
            bfs = [p[0]] #�̶�����ĸ
            for char in p[1:]:
                bfs += [s + char for s in bfs] #����64�ֿ���
            cnt = 0
            for combination in bfs:
                tmp = "".join(sorted(combination))
                if tmp in record: #������ǰ�����words����û�г��ֹ�
                    cnt += record[tmp]
            res.append(cnt)
        return res
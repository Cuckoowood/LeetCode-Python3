class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        from collections import defaultdict
        start = defaultdict(list)
        end = defaultdict(list)
        for i, phrase in enumerate(phrases):
            t = phrase.split(" ")
            start[t[0]].append((phrase, i))
            end[t[-1]].append((phrase, i))
        res = []
        for key, val in end.items():
            val.sort() #����֤�������ֵ�������
        for key, val in start.items():
            val.sort() #����֤�������ֵ�������
        for end_word, p1 in end.items():
            if end_word in start: #�ҵ�����ƴ�ӵĲ���
                for s1, i1 in p1:
                    for s2, i2 in start[end_word]:
                        if i1 == i2: #������Ŀ���� ���� �������
                            continue
                        if len(s2.split(" ")) == 1: #���s2ֻ��һ�����ʹ��ɣ���ôֱ�ӷ���s1
                            tmp = s1
                        else:
                            tmp = s1 + " " + " ".join(s2.split(" ")[1:])
                        if tmp not in res:
                            res.append(tmp)
        res.sort()
        return res


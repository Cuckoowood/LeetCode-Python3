class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        flatten = sum(mat,[])  # �Ѷ�ά����չ����һά
        dic = Counter(flatten) # ͳ������Ԫ��Ƶ��
        for num in mat[0]: # �ڵ�һ��Ԫ��������û�г���Ƶ�ʵ���mat������Ԫ��
            if dic[num] == len(mat): # ��һ������������Ԫ�ؾ��Ǵ�
                return num
        return -1
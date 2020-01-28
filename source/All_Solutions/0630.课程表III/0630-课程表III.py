class Solution:
    def scheduleCourse(self, courses):  # �Խ���ʱ���������У������ǰtС�ڽ���������tֵ���滻��ɰ�����ɣ����滻
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        def siftdown(A, index):
            lenA = len(A)
            i = (index<<1) + 1 if index else 1
            while i < lenA:  # С���³�
                if i+1 < lenA and A[i+1]>A[i]:
                    i += 1
                if A[index] < A[i]:
                    A[index], A[i] = A[i], A[index]
                    index = i
                    i = (index<<1) + 1
                else:
                    break
        
        def siftup(A, index):
            while index:
                i = (index - 1)>>1
                if A[i] < A[index]:  # �����ϸ�
                    A[index], A[i] = A[i], A[index]
                    index = i
                else:
                    break
                
        courses.sort(key = lambda x: x[1])
        cur = res = 0
        tmp = []  # �ö��������
        for t, d in courses:
            if cur + t <= d:
                cur += t
                tmp.append(t)
                siftup(tmp, res)
                res += 1
            elif tmp and t<tmp[0] and cur - tmp[0] + t <= d:  # ע��
                cur += t - tmp[0]
                tmp[0] = t
                siftdown(tmp, 0)
        return res
        
class Solution:
    def getImportance(self, employees, id):

        importance = {e.id: e.importance for e in employees}        # ��Ҫ���ֵ�{Ա��: ��Ҫ��}
        subordinates = {e.id: e.subordinates for e in employees}    # �����ֵ�{Ա��: �����б�}

        def get_subordinates(id):                   # ���Ա����ֱ����������
            all_staff = []                          # ����б�
            queue = [id]                            # �������
            while queue:                            # ֻҪ���в�Ϊ��
                staff = queue.pop(0)                # ��βԪ�س���
                all_staff.append(staff)             # ������뵽����б���
                queue.extend(subordinates[staff])   # ��Ա���������������
            return all_staff                        # ��������Ա������

        return sum([importance[staff] for staff in get_subordinates(id)]) 
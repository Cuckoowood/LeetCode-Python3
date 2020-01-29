class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        if not root:
            return False
        queue = [root]
        while queue:
            # ѭ����ʼʱ�������е�Ԫ�ظ������ǵ�ǰ����ĸ���
            size = len(queue)
            # ��һ��Ľ��ֵ���Ž�������������ս�㣬���� 0��
            # ��Ŀ��˵"ÿ���ڵ��ֵ����Ψһ�ġ���ΧΪ 1 �� 100 ��������"
            # ���ԣ���� 101 ���ǿ��Ե�
            cur_level = []
            for _ in range(size):
                top = queue.pop(0)
                if top:
                    cur_level.append(top.val)
                    queue.append(top.left)
                    queue.append(top.right)
                else:
                    cur_level.append(0)

            # �����������������һ�㣬ֻ��һ�������Ҫ�ų�
            # �Ǿ���������㰤�ţ���������С�Ľ������������ż��
            if x in cur_level and y in cur_level:
                index1 = cur_level.index(x)
                index2 = cur_level.index(y)
                if index1 > index2:
                    index1, index2 = index2, index1
                if index1 + 1 == index2 and index1 & 1 == 0:
                    return False
                return True
            # �����������ͬһ�㣬ֱ�ӾͿ��Է��ز������ֵܽ����
            if x in cur_level or y in cur_level:
                return False
        return False
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        record = []
        sm = 0
        result = 0
        
        # ʹ��������������
        while record or root:
            while root:
                sm = 2*sm + root.val
                record.append([root, sm])
                root = root.left
            
            # ������Ѿ����������󣬿�ʼͨ��pop����root���򷵻ر���ʱ
            # �Ͳ���ִ�������while����ֱ��pop�����¸�sm��ֵ
            # ����record���sm�����õ�
            node, sm = record.pop()
            
            # ֻ�е�Ҷ�ӽڵ�Ž�����ۼӵ�result
            if not node.left and not node.right:
                result += sm
            
            root = node.right
        
        return result
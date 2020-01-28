class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []                                 

        cur_layer = [root]                            
        res = []                                        # ����б���Ÿ����ֵ
        while cur_layer:                         
            # ����ǰ����ƽ��ֵ��ӵ������
            res.append(sum(node.val for node in cur_layer) / len(cur_layer))

            next_layer = []                             
            for node in cur_layer:                      # ������һ�����б��еĸ������

                if node.left:                           # �������������
                    next_layer.append(node.left)        # ������ӵ���һ���б�
                if node.right:                 
                    next_layer.append(node.right) 

            cur_layer = next_layer                      # ������һ�����б�

        return res   
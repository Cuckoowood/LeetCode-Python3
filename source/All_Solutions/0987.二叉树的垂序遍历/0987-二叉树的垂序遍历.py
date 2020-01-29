class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        # �ֵ�d��key��Ž�㣬value��Ÿý���x��y�����Լ���������������ʵ���index
        self.d = {} # node: (x, y, index)
        
        def dfs(root, x, y, idx):
            if not root:
                return 
            self.d[root] = [x, y, idx]
            dfs(root.left, x-1, y-1, idx+1)
            dfs(root.right, x+1, y-1, idx+2)
        dfs(root, 0, 0, 0)

        # ����ϸ�ڣ����׳���
        # 1.�� x ��С�����ţ��൱�ڴ������Ҵ�ֱ������
        # 2.�� y �Ӵ�С�ţ�����x������ͬʱ�ȳ��ֵĵ㣨y�����ȼ����б�
        # 3.��x��y����ͬʱ����������ȫһ������������ֵ��С��������
        dd = sorted(self.d.items(), key=lambda x: (x[1][0], -x[1][1], x[0].val)) # dd���ͣ�list
        res, tmp = [],[]
        pre = dd[0][1][0] # pre �����жϵ�ǰ���ʵĽ�����һ������Ƿ���ͬһ����ֱ����
        for item in dd:
            node, pos = item
            if pos[0] == pre:
                tmp.append(node.val)
            else:
                res.append(tmp)
                pre = pos[0]
                tmp = [node.val]
        if tmp: # ���� tmp �п��ܻ��в��������ϣ�
            res.append(tmp)
        return res


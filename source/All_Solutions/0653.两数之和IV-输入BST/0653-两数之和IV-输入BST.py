# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False

        # �����������
        def dfs(node):
            # targetĿ��ֵ�뵱ǰֵ���
            if k - node.val in exist:
                self.res = True
                return 
            else:
                exist.add(node.val)

            # ��ǰû�з��ϵ����������ݣ�����
            if not self.res: 
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)

        exist = set()
        self.res = False
        dfs(root)
        return self.res
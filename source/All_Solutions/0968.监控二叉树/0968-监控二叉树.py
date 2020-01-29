# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        self.ans = 0
        if self.dfs(root)==2:
            self.ans+=1
        return self.ans
    
    
    #0�� �ý�㸽����δ�����ӽ�㣬��װ�����
    #1���ý����Χ�м������ý�㲻���ڣ������ð�װ�����
    #2���ý�㸽��û�м��������ʾ�丽����Ҫ�����
    def dfs(self,root):
        if not root:
            return 1
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l==2 or r==2:
            self.ans+=1
            return 0
        elif l==0 or r==0:
            return 1
        else:
            return 2
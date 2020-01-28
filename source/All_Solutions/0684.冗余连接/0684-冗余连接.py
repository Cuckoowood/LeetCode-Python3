class Solution:
    """���鼯"""
    '''
    ��¼1��N��ÿ�����ĸ�����Ϊ����л������»�������[u, v]һ������ͬ��root��
    ���ǿ������Ϊ��һ���ڵ��������֧��ͨ��[u,v]���������ˣ���Ȼ������һ���ڵ��������֧����ô����һ������ͬ��root������ֱ���Ƴ�[u,v]�ͺ�����
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges)+1)]

        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        
        for u, v in edges:
            u_parent = find(u)
            v_parent = find(v)
            if u_parent != v_parent:
                root[v_parent] = u_parent
            else:
                return [u, v]
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        ˼·:Ⱦɫ��,
        1.��ĳһ���̶��ڵ����,�������ڵĵ㶼Ⱦ���෴����ɫ,Ȼ������ڵĵ��������,�ظ�1
        �������������ڵ����ɫ��ͬ����,���Ƕ���ͼ
        '''
        color = [0] * len(graph)
        def color_node(node):
            nonlocal color
            queue = [node]
            color[node] = 1
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 1 if color[node] == -1 else -1
                        queue.append(neighbor)
                    if color[neighbor] + color[node] != 0:
                        return False
            return True
        for node in range(len(graph)):
            if color[node] == 0:
                color_res = color_node(node)
                if not color_res:
                    return False
        return True
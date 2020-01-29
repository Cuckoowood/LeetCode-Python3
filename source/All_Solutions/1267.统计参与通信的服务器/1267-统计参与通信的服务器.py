"""
DFS���൱��һ������ͨ���������Ŀ
"""
from collections import defaultdict
class Solution:
    def countServers(self, grid) -> int:
        col = defaultdict(list)
        row = defaultdict(list)
        mat = defaultdict(list)
        vis, node = set(), []
        # ����ͨ������
        def DFS(node, area):
            for i in mat[node]:
                if i not in vis:
                    vis.add(i)
                    area += DFS(i, 1)
            return area
        # ��ͼ
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    node.append((x, y))
                    row[x].append((x, y))
                    col[y].append((x, y))
        for i in node:
            if row.get(i[0]):
                for j in row.get(i[0]):
                    if j != i and j not in mat[i]:
                        mat[i].append(j)
            if col.get(i[1]):
                for j in col.get(i[1]):
                    if j != i and j not in mat[i]:
                        mat[i].append(j)
        # �������ͨ������
        res = 0
        for i in node:
            if i not in vis and mat[i]:
                vis.add(i)
                res += DFS(i, 1)
        return res
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = board[0]+board[1]  # ��board��������һά
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]  # ÿ��λ�õ�0���Խ�����λ��
        q, visited = [(tuple(board), board.index(0), 0)], set()  # bfs�Ķ��к��ѷ���״̬��¼
        while q:
            state, now, step = q.pop(0)  # �ֱ����ǰ״̬��0�ĵ�ǰλ�ú͵�ǰ����
            if state == (1, 2, 3, 4, 5, 0):  # �ҵ���
                return step
            for next in moves[now]:  # �������пɽ���λ��
                _state = list(state)
                _state[next], _state[now] = _state[now], state[next]  # ����λ��
                _state = tuple(_state)
                if _state not in visited:  # ȷ��δ����
                    q.append((_state, next, step+1))
            visited.add(state)
        return -1
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # ������������λ��, �õ�һ�����ο������
        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)
        # û���ص������
        if B >= H or D <= F or C <= E:
            return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
        # �ص����
        # �±߽�
        down = max(A, E)
        # ��
        up = min(C, G)
        # ��
        left = max(B, F)
        # ��
        right = min(D, H)
        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - abs(up - down) * abs(left - right)

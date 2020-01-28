
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
            # ��ɢ��
            index_set = set()
            for pos in positions:
                index_set.add(pos[0])
                index_set.add(pos[0] + pos[1] - 1)
            index_set = sorted(list(index_set))
            
            index_map = {val: idx for idx, val in enumerate(index_set)}
            
            ans = []
            res = 0
            ground = [0 for _ in range(len(index_map))]
            for pos in positions:
                x, y = index_map[pos[0]], index_map[pos[0] + pos[1] - 1]
                # �����һ���Ż�, ����Ĳ�ѯmax��update�������߶�������
                max_cur = max(ground[x : y + 1])
                cur_res = max_cur + pos[1]
                for idx in range(x, y + 1):
                    ground[idx] = cur_res
                
                res = max(cur_res, res)
                ans.append(res)
            return ans
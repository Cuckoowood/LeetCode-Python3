class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping(special, needs):  # ��special��պù���needs�������ͻ���
            if not sum(needs):  # needs��û��
                return 0
            # �ȹ��˵�special���Ѿ���ĳһ����Ʒ������needs�����
            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(l)), special))
            if not special:  # ������˺�Ϊ�գ���ô����ֱ���Ե�Ʒ����needs�ļ۸�
                return sum(needs[i]*price[i] for i in range(l))
            res = []
            for pac in special:  # ���ݣ��ռ����ι���ÿ������Ļ��Ѽ���������������ʣ��needs�ݹ����ͻ���
                res.append(pac[-1]+shopping(special, [needs[i]-pac[i] for i in range(l)]))
            return min(res)  # ���ر��ι���ļ���ѡ���е���ͻ���

        l = len(price)
        # �ȹ��˵�����ԭ����������
        special = list(filter(lambda x: x[-1] < sum(x[i]*price[i] for i in range(l)), special))
        return shopping(special, needs)
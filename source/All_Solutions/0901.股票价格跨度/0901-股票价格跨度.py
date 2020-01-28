class StockSpanner:
    """
    ��һ��ջ���洢��ȥ��Ʊ�ļ۸�Ͷ�Ӧ�Ŀ�ȣ�
    �������Ĺ�Ʊ�۸����ջ���Ĺ�Ʊ�۸����ջ��
    ����Ӧ�Ŀ�ȼӵ����չ�Ʊ�۸�Ŀ���ϣ�
    ֱ��ջ���Ĺ�Ʊ�۸���ڵ��չ�Ʊ�۸�Ȼ�󽫵��չ�Ʊ�۸�Ͷ�Ӧ�Ŀ����ջ
    """
    def __init__(self):
        self.his_prices = [(-999, 0)]

    def next(self, price: int) -> int:
        span = 1
        while self.his_prices:
            if self.his_prices[-1][0] <= price:
                span += self.his_prices.pop()[1]
            else:
                break
        self.his_prices.append((price, span))
        return span
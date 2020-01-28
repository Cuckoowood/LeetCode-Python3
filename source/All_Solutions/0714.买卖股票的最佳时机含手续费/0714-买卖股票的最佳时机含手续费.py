class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        dp1 = [0 for _ in range(n)]#��i�������й�Ʊʱ���������
        dp2 = [0 for _ in range(n)]#��i�������޹�Ʊʱ���������
        dp1[0] = -prices[0]
        for i in range(1,n):
            dp1[i] = max(dp1[i-1], dp2[i-1] - prices[i])
            dp2[i] = max(dp2[i-1], dp1[i-1] + prices[i] - fee)
        return dp2[n-1]
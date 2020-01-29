class Solution:

    def numPrimeArrangements(self, n: int) -> int:
       
        cnt_p = 0 #�����ĸ���
        sum_p = 1 #�����ĸ���ȫ���к�
        
        cnt_n = 1 #�������ĸ���
        sum_n = 1 #�������ĸ���ȫ���еĺ�
        
        for i in range(2, n + 1): 
            if self.isPrime(i):
                cnt_p += 1
                sum_p *= cnt_p
            else:
                cnt_n += 1
                sum_n *= cnt_n
        
        #����������ȫ���� * ������������ȫ����
        return (sum_p * sum_n) % (10**9 + 7)
        
    def isPrime(self, num: int) -> bool:
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True     
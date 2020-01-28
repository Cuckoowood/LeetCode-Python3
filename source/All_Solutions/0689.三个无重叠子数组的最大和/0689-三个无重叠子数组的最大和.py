class Solution:
    def maxSumOfThreeSubarrays(self, nums: [int], k: int) -> [int]:
        n = len(nums)
        l = n - k + 1     
        sums = [0] * l      #����ÿ������Ϊk��������ĺ�
        s = sum(nums[:k])
        sums[0] = s
        for i in range(1,l):
            s = s + nums[i+k-1] - nums[i-1]
            sums[i] = s

        #�м�������Ϊiʱ��������Ŀ�ʼλ��
        mid = {i:0 for i in range(k,l)}   #��ʼ��Ϊ0
        for i in range(k, l):
            j = mid.get(i-1,0)
            if sums[i-k] > sums[j]: #��֤�м����鿪ʼΪiʱ��������Ϊ����
                j = i-k
            mid[i] = j  #�м������鿪ʼΪiʱ�������鿪ʼΪj

        #�������鿪ʼΪiʱ�м������鿪ʼλ��
        right = {i:k for i in range(2*k,l)} #��ʼ��Ϊk
        res = [0, k, 2 * k]
        for r in range(2 * k, l):
            m = right.get(r-1,k)
            #���������鿪ʼ�±�Ϊrʱ����ʱ�����������м������������
            if sums[r-k]+sums[mid[r-k]] > sums[m]+sums[mid[m]]:
                m = r - k
            right[r] = m    #�������鿪ʼ�±�Ϊrʱ�м����鿪ʼ�±�Ϊm
            if sums[r]+sums[m]+sums[mid[m]] > sums[res[0]]+sums[res[1]]+sums[res[2]]:
                res = [mid[m], m, r]
        return res
class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        //С���ѣ��Ѷ�Ϊ���б���С��ǰԪ�� ��ά����
        Queue<int[]> minQueue = new PriorityQueue<>(Comparator.comparingInt(arr -> nums.get(arr[0]).get(arr[1])));
        //����ѣ��Ѷ�Ϊ���б����ǰԪ�� ��ά����
        Queue<int[]> maxQueue = new PriorityQueue<>((arr1, arr2) -> nums.get(arr2[0]).get(arr2[1]) - nums.get(arr1[0]).get(arr1[1]));
        int[] ans = new int[]{Integer.MIN_VALUE, Integer.MAX_VALUE};
        for (int i = 0; i < nums.size(); i++) {
            //��ʼ�����б��һ��Ԫ�أ�С����&��������ͬһ�����󣬷������remove
            int[] arr = new int[]{i, 0};
            minQueue.offer(arr);
            maxQueue.offer(arr);
        }
        while (minQueue.size() == nums.size()) {
            //�Ƴ�С���Ѷ�Ԫ�أ�С����size-1
            int[] minArr = minQueue.poll();
            //С���Ѷ�Ԫ�������Ѷ�Ԫ�����䣬ÿ���б�������һ��������������
            int[] maxArr = maxQueue.peek();
            //ע��˴����ֵ�������Ҫת��long
            if ((long) nums.get(maxArr[0]).get(maxArr[1]) - (long) nums.get(minArr[0]).get(minArr[1]) < (long) ans[1] - (long) ans[0]) {
                ans[0] = nums.get(minArr[0]).get(minArr[1]);
                ans[1] = nums.get(maxArr[0]).get(maxArr[1]);
            }
            //����С���Ѷ�Ԫ�أ�ȡ�������б���һԪ�����¹�����
            if (minArr[1] < nums.get(minArr[0]).size() - 1) {
                int[] newArr = new int[] {minArr[0], minArr[1] + 1};
                minQueue.offer(newArr);
                //��Ϊ�����ͬ���󣬿���ֱ��remove
                maxQueue.remove(minArr);
                maxQueue.offer(newArr);
            }
        }
        return ans;
    }
}


class Solution {
    public List<Integer> countSteppingNumbers(int low, int high) {
        Queue<Integer> temp = new LinkedList<>();
        List<Integer> result = new ArrayList<Integer>();
        addElementBFS(temp,result,low,high);
        return result;
    }

    //��Ϊ�����������������һ�������ȥ�������˳����������
    public static void addElementBFS(Queue<Integer> temp,List<Integer> res,int low,int high){
        if(low == 0){//���low==0���ڽ����0
            res.add(0);
        }

        for(int i=1;i<=9;i++){//1��9��������
            temp.add(i);
        }
        
        while(temp != null){
            int t= temp.poll();//ȡ�б�ͷԪ��
            int end = t;//��λ��ĩλΪ����
            if(t>=10){
                end = t%10;//�ǵ�λ��ĩλ����
            }
            if(t > high){//Ԫ�س�����Χ�˳�
                break;
            }
            if(t>=low && t<=high){
                res.add(t);//����������ٷ�Χ�ھ����
            }
            if(end != 0){//����10��������99
                temp.add(t*10 + (end-1));
            }
            if(end != 9){//����9��������100
                temp.add(t*10 + (end+1));
            }
        }
    }
}
//�˹������������ָ����������call��

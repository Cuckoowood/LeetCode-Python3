# �����maxLevl=16��power=2�����������������maxRand
maxLevel = 16
power = 2
maxRand = power ** maxLevel - 1
# ���������������൱��[1 ... 65535]ȡ�����Ȼ���ٶ�2ȡ�������ɱ�֤���������[1 ... 16]��Щ�������ָ���ֲ�
randLevel = lambda: maxLevel - int(math.log(random.randint(1, maxRand), power))

# �������ԣ��������ֵ�����ҵ�ָ�룬���µ�ָ��
class SkipNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        # ��ʼ��������������ǽ��
        left = [SkipNode(-float('inf')) for _ in range(maxLevel)]
        right = [SkipNode(float('inf')) for _ in range(maxLevel)]
        # ��ǽ�ڽ�����һ��
        for i in range(maxLevel - 1):
            left[i].right = right[i]
            left[i].down = left[i + 1]
            right[i].down = right[i + 1]
        # ���һ�㵥������ֻ������ָ��û������ָ��
        left[-1].right = right[-1]
        # �����ʼָ��Ϊ��ڵ���Ԫ��
        self.head = left[0]

    def search(self, target: int) -> bool:
        # �ӳ�ʼָ�뿪ʼ������Ծ�������Ҳ�����node����ΪNone������ѭ���Զ�����None�����ϲ��Ժ�False�ȼ�
        node = self.head
        while node:
            if node.right.value > target:
                node = node.down
            elif node.right.value < target:
                node = node.right
            else:
                return True

    def add(self, num: int) -> None:
        # ��prev����洢������Ծǰ������ָ�룬����֮�����ָ��ʱǰ��������ȥ˫��ָ�봦��
        prev = []
        # ԭ��������ָ�����
        node = self.head
        while node:
            # �����ұߴ��ڵ����Լ�ʱ��������������prev����������ָ������
            if node.right.value >= num:
                prev.append(node)
                node = node.down
            else:
                node = node.right
        # �������ָ�����飬���Ȱ����ʽ������
        arr = [SkipNode(num) for _ in range(randLevel())]
        # ��zip��prev������Ԫ�����µ�ָ�����齻����һ�μ�������������
        t = SkipNode(None)
        for p, a in zip(prev[maxLevel - len(arr): ], arr):
            a.right = p.right
            p.right = a
            t.down = a
            t = a

    def erase(self, num: int) -> bool:
        # ansΪ�����־��erase�Ľṹ��search�ṹ���ƣ�������ָ�����
        ans = False
        node = self.head
        while node:
            if node.right.value > num:
                node = node.down
            elif node.right.value < num:
                node = node.right
            else:
                # �������ʱ���޸������־
                ans = True
                # ɾ��node.right���������еĹ�ϵ
                node.right = node.right.right
                node = node.down
        return ans


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # ��ʼ��ջ
        stack = []
        # ����ջԪ��
        for e in S:
            if stack and stack[-1] == e:
                stack.pop()
            else:
                stack.append(e)
        return "".join(stack)
                    
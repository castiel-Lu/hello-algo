# 栈是一种先进后出的线性数据结构
class ListNode(object):
    def __init__(self, val: int):
        self.val = val
        self.next: ListNode = None
class LinkedListStack(object):
    def __init__(self):
        self._peek: ListNode = None
        self._size: int = 0

    def size(self):
        return self._size

    def is_empty(self):
        # 检查栈顶是否为None
        return not self._peek

    def push(self, val: int) -> None:
        # 推入一个值到栈
        # 创建一个节点并赋值
        node = ListNode(val)
        # 新值的下一个节点指向原来的头节点，如果原来不存在节点，那就是None
        node.next = self._peek
        # 头节点设置为新值
        self._peek = node
        # 栈的长度+1
        self._size += 1

    def pop(self) -> int:
        # 保存头节点的值
        num = self.peek()
        # 将头节点设置为原来的下一个节点，即首节点被删除了
        self._peek = self._peek.next
        # 整个栈的长度-1
        self._size -= 1
        # 返回pop出的节点的值
        return num

    def peek(self) -> int:
        # 如果栈为空，报错
        if self.is_empty():
            raise IndexError('栈为空')
        # 否则返回栈顶节点的值
        return self._peek.val

    def to_list(self) -> list[int]:
        arr = []
        # 先取链表的第一个节点
        node = self._peek
        # 当还有节点存在
        while node:
            # 数组将节点的值依次保存
            arr.append(node.val)
            # 节点下移
            node = node.next
        # 将列表顺序反转，列表存储的值按栈底到栈顶顺序排列
        arr.reverse()
        return arr

class ArrayStack(object):
    def __init__(self):
        self._stack: list[int] = []

    def size(self):
        return len(self._stack)

    def is_empty(self):
        return self._stack == []

    def push(self, val: int) -> None:
        self._stack.append(val)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('栈为空')
        self._stack.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('栈为空')
        return self._stack[-1]

    def to_list(self) -> list[int]:
        return self._stack

if __name__ == '__main__':
    # stack: list[int] = []
    #
    # stack.append(1)
    # stack.append(3)
    # stack.append(2)
    # stack.append(5)
    # stack.append(4)
    #
    # peek: int = stack[-1]
    #
    # pop: int = stack.pop()
    #
    # size: int = len(stack)
    #
    # is_empty: bool = len(stack) == 0

    print("使用链表底层数据结构：")
    stack1 = LinkedListStack()
    stack1.push(1)
    stack1.push(3)
    stack1.push(2)
    stack1.push(5)
    stack1.push(4)
    print("最初的栈为：{}".format(stack1.to_list()))
    num = stack1.pop()
    print("推出栈顶，其值为：{}".format(num))
    print("现在的栈为：{}".format(stack1.to_list()))
    print("现在的栈顶为：{}".format(stack1.peek()))
    print("栈是否为空：{}".format(stack1.is_empty()))
    print("现在栈的元素共{}个".format(stack1.size()))

    print()

    print("使用数组底层数据结构：")
    stack2 = ArrayStack()
    stack2.push(1)
    stack2.push(3)
    stack2.push(2)
    stack2.push(5)
    stack2.push(4)
    print("最初的栈为：{}".format(stack2.to_list()))
    num = stack2.pop()
    print("推出栈顶，其值为：{}".format(num))
    print("现在的栈为：{}".format(stack2.to_list()))
    print("现在的栈顶为：{}".format(stack2.peek()))
    print("栈是否为空：{}".format(stack2.is_empty()))
    print("现在栈的元素共{}个".format(stack2.size()))
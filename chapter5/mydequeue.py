# 双向队列允许在头部和尾部执行元素的添加或删除操作

class ListNode(object):
    def __init__(self, val:int ):
        self.val = val
        self.next = None
        self.prev = None

class LinkedListDeque(object):
    "基于链表的双向队列"
    def __init__(self):
        self._front: ListNode = None
        self._rear: ListNode = None
        self._size: int = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, num: int, is_front: bool):
        # 创建一个新节点，值为num
        node = ListNode(num)
        # 如果队列为空，则插入的节点的头尾节点都是它
        if self.is_empty():
            self._front = node
            self._rear = node
        elif is_front:
            # 如果要求从前插入
            # 则原来头节点的前一个节点现在是node，它现在变为第二个节点
            self._front.prev = node
            # node节点即现在的头节点的下一个节点应该是原来的头节点
            node.next = self._front
            # 头节点更新为新插入的节点node
            self._front = node
        else:
            # 如果要求从尾插入
            # 则原来的尾节点的下一个节点是新插入的node节点
            self._rear.next = node
            # 插入的node节点的前一个节点是原来的尾节点
            node.prev = self._rear
            # 更新尾节点是node
            self._rear = node
        self._size += 1

    def push_frist(self, num: int):
        self.push(num, True)

    def push_last(self, num: int):
        self.push(num, False)

    def pop(self, is_front: bool):
        # 如果队列为空，报错
        if is_empty:
            raise IndexError('双向队列为空')
        if is_front:
            # 如果是前向出队
            # 保留要出队的头节点的值
            val = self._front.val
            # 保存头节点的下一个节点
            fnext = self._front.next
            # 如果下一个节点存在
            if fnext != None:
                # 则头节点出队后，第二个节点的前节点应该为None
                fnext.prev = None
                # 设置头节点的下一个节点为None，表示被删除了
                self._front.next = None
            # 删除原来的头节点后，队列新的头节点就是原本的下一个节点
            self._front = fnext
        else:
            # 保存原本的尾节点的值
            val = self._rear.val
            # 取出原尾节点之前的一个节点
            rprev = self._rear.prev
            if rprev != None:
                # 将其的指向的下一个节点设置为空
                rprev.next = None
                # 原本的尾节点的指向前一个节点设置为空，这样原本的尾节点就被删除了
                self._rear.prev = None
            # 更新删除后的尾节点为rprev
            self._rear = rprev
        # 队列长度-1
        self._size -= 1
        return val

    def pop_front(self):
        return self.pop(True)

    def pop_last(self):
        return self.pop(False)

    def peek_first(self):
        if self.is_empty():
            raise IndexError('双向队列为空')
        return self._front.val

    def peek_last(self):
        if self.is_empty():
            raise IndexError('双向队列为空')
        return self._rear.val

    def to_array(self):
        # 从头节点开始
        node = self._front
        # 设置一个队列长度的空数组
        res = [0] * self.size()
        for i in range(self.size()):
            res[i] = node.val
            node = node.next
        return res

class ListDeque(object):
    def __init__(self, capacity: int):
        # 初始化一个指定容量的空数组
        self._nums = [0] * capacity
        # 保存头节点的索引
        self._front = 0
        # 保存数组的长度
        self._size = 0

    def capacity(self):
        return len(self._nums)
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def index(self, i:int ):
        # 让首节点指针可以返回
        return (i + self.capacity()) % self._size

    def push_frist(self, num: int):
        if self.size() == self.capacity():
            raise IndexError('双向队列已满')
        # 获取头节点的索引
        self._front = self.index(self._front - 1)
        # 赋值
        self._nums[self._front] = num
        self._size += 1

    def push_last(self, num: int):
        if self.size() == self.capacity():
            raise IndexError('双向队列已满')
        # 尾部的索引等于头节点索引+队列长度
        rear = self.index(self._front + self._size)
        self._nums[rear] = num
        self._size += 1

    def pop_frist(self):
        # 先获取头节点的值
        num = self.peek_first()
        # 头节点索引+1，表示原来的头节点被删除
        self._front = self.index(self._front + 1)
        self._size -= 1
        return num

    def pop_last(self):
        # 获取尾节点的值
        num = self.peek_last()
        # 队列长度-1
        self._size -= 1
        return num

    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError('双向队列为空')
        return self._nums[self._front]

    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError('双向队列为空')
        # 尾部的索引值-1，表示尾节点被删除
        last = self.index(self._front + self._size -1)
        return self._nums[last]

    def to_array(self):
        res = []
        for i in range(self.size()):
            res.append(self._nums[self.index(self._front + i)])
        return res




if __name__ == '__main__':
    from collections import deque
    print("使用collections.deque实现：")
    deque= deque()
    # 从后面添加入队
    deque.append(2)
    deque.append(5)
    deque.append(4)
    # 从队列头入队
    deque.appendleft(3)
    deque.appendleft(1)
    print("队列为：{}".format(deque))
    front: int = deque[0]
    print("队首值为：{}".format(front))
    rear: int = deque[-1]
    print("队尾值为：{}".format(rear))
    pop_front: int = deque.popleft()
    print("队首出队：{}".format(pop_front))
    pop_rear: int = deque.pop()
    print("队尾出队：{}".format(pop_rear))
    size: int = len(deque)
    print("队列长度：{}".format(size))
    is_empty: bool = len(deque) == 0
    print("队列是否为空：{}".format(is_empty))

    print()

    print("基于链表实现的双向队列：")
    deque1 = LinkedListDeque()
    deque1.push_last(2)
    deque1.push_last(5)
    deque1.push_last(4)
    deque1.push_frist(3)
    deque1.push_frist(1)
    print("队列为：{}".format(deque1.to_array()))
    front: int = deque1.peek_first()
    print("队首值为：{}".format(front))
    rear: int = deque1.peek_last()
    print("队尾值为：{}".format(rear))
    pop_front: int = deque1.pop_front()
    print("队首出队：{}".format(pop_front))
    pop_rear: int = deque1.pop_last()
    print("队尾出队：{}".format(pop_rear))
    size: int = deque1.size()
    print("队列长度：{}".format(size))
    is_empty: bool = deque1.is_empty()
    print("队列是否为空：{}".format(is_empty))

    print()
    print("基于数组实现的双向队列：")
    deque2 = LinkedListDeque()
    deque2.push_last(2)
    deque2.push_last(5)
    deque2.push_last(4)
    deque2.push_frist(3)
    deque2.push_frist(1)
    print("队列为：{}".format(deque2.to_array()))
    front: int = deque2.peek_first()
    print("队首值为：{}".format(front))
    rear: int = deque2.peek_last()
    print("队尾值为：{}".format(rear))
    pop_front: int = deque2.pop_front()
    print("队首出队：{}".format(pop_front))
    pop_rear: int = deque2.pop_last()
    print("队尾出队：{}".format(pop_rear))
    size: int = deque2.size()
    print("队列长度：{}".format(size))
    is_empty: bool = deque2.is_empty()
    print("队列是否为空：{}".format(is_empty))
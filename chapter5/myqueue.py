# 队列是一种先进先出的线性数据结构
# 队列头部称为队首，队列尾部称为队尾，元素加入队尾的过程称为入队，删除队首元素的操作称为出队
# 主要方法
# push() 元素入队，即将元素加至队尾
# pop() 队首元素出队
# peek() 访问队首元素

class ListNode(object):
    def __init__(self, val: int):
        self.val = val
        self.front: ListNode = None
        self.next: ListNode = None
        self.rear: ListNode = None

class LinkedListQueue(object):
    def __init__(self):
        # 头节点front
        self._front: ListNode = None
        # 尾节点rear
        self._rear: ListNode = None
        self._size: int = 0

    def size(self):
        return self._size

    def is_empty(self) -> bool:
        return not self._front

    def push(self, num: int):
        # 设置一个节点，值为num
        node = ListNode(num)
        # 如果头节点为None，那么设置头尾节点都为node
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            # 如果头节点不为None
            # 设置添加前的尾节点的下一个节点为node，本来尾节点的next是None，即将节点添加到尾节点之后
            self._rear.next = node
            # 将添加后的链表的尾节点设置为node节点
            self._rear = node
        # 队列大小+1
        self._size += 1

    def pop(self) -> int:
        # 先获取头节点的值
        num = self.peek()
        # 因为先执行了peek函数，所以不用考虑队列为空，直接将头节点赋值为下一个节点
        # 如果队列只有1个节点，那么其next为None
        self._front = self._front.next
        # 队列长度-1
        self._size -= 1
        # 返回头节点的值
        return num

    def peek(self) -> int:
        # 如果队列为空，报队列为空错误
        if self.is_empty():
            raise IndexError('队列为空')
        # 返回头节点的值
        return self._front.val

    def to_list(self):
        queue = []
        # 从头节点开始遍历
        temp = self._front
        while temp:
            # 将队列的值依次放入列表内
            queue.append(temp.val)
            temp = temp.next
        return queue

# 在数组中删除首元素的时间复杂度为O(n)，会导致出队操作效率低
# 使用一个变量front指向队首元素的索引，并维护一个变量size用于记录队列长度
# 定义rear = front + size，计算队尾元素之后的下一个位置
# 另外随着入队和出队，front和rear都在向右移动，我们需要让其在越过数组尾部时，直接回到数组头部继续遍历，使用取余实现
class ListQueue(object):
    def __init__(self, size: int):
        # 初始化一个size大小的容量空列表
        self._nums = [0] * size
        # 设置_front指针指向队首
        self._front: int = 0
        # 设置队列长度
        self._size: int = 0

    def capacity(self) -> int:
        # 返回队列容量
        return len(self._nums)

    def size(self):
        # 返回队列大小
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, num: int):
        # 如果队列容量等于队列大小，报队列已满
        if self._size == self.capacity():
            raise IndexError('队列已满')
        # 指定rear指针指向队列尾部，取余循环
        # 比如说现在队列只有一个元素，队列长度为5，尾节点索引为(0+1)%5=1
        rear: int = (self._front + self._size) % self.capacity()
        # 将值放入队列尾部
        self._nums[rear] = num
        # 队列的值+1
        self._size += 1

    def pop(self) -> int:
        # 先取出队列头部的元素的值
        num: int = self.peek()
        # 则新的头节点应该是下一个节点即（0+1）%5=1 索引上的元素，将它设置为头节点
        self._front = (self._front + 1) % self.capacity()
        # 队列大小-1
        self._size -= 1
        return num

    def peek(self) -> int:
        # 如果队列为空，则报错
        if self.is_empty():
            raise IndexError('队列为空')
        # 返回头节点的值
        return self._nums[self._front]

    def to_list(self):
        # 初始化一个队列长度的空列表
        res = [0] * self.size()
        # 从头节点开始遍历
        j: int = self._front
        for i in range(self.size()):
            # 保存队列内的值
            res[i] = self._nums[(j % self.capacity())]
            j += 1
        return res


if __name__ == '__main__':
    print("直接使用标准库的collections.deque：")
    from collections import deque

    que = deque()
    que.append(1)
    que.append(3)
    que.append(2)
    que.append(5)
    que.append(4)

    print("队列的值为：{}".format(que))
    is_empty: bool = len(que) == 0
    print("队列是否为空：{}".format(is_empty))
    front: int = que[0]
    print("队列的头节点为：{}".format(front))
    pop: int = que.popleft()
    print("出队的值为：{}".format(pop))
    print("队列的值为：{}".format(que))
    size: int = len(que)
    print("队列大小为：{}".format(size))

    print()

    print("基于链表的队列实现测试：")
    que1: LinkedListQueue = LinkedListQueue()
    que1.push(1)
    que1.push(3)
    que1.push(2)
    que1.push(5)
    que1.push(4)
    print("队列的值为：{}".format(que1.to_list()))
    print("队列是否为空：{}".format(que1.is_empty()))
    print("队列的头节点为：{}".format(que1.peek()))
    num = que1.pop()
    print("出队的值为：{}".format(num))
    print("此时队列的值为：{}".format(que1.to_list()))
    print("队列大小为：{}".format(que1.size()))

    print()

    print("基于数组的队列实现测试：")
    que2: ListQueue = ListQueue(5)
    que2.push(1)
    que2.push(3)
    que2.push(2)
    que2.push(5)
    que2.push(4)
    print("队列的值为：{}".format(que2.to_list()))
    print("队列是否为空：{}".format(que2.is_empty()))
    print("队列的头节点为：{}".format(que2.peek()))
    num = que2.pop()
    print("出队的值为：{}".format(num))
    print("此时队列的值为：{}".format(que2.to_list()))
    print("队列大小为：{}".format(que2.size()))
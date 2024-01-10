# 双向队列允许在头部和尾部执行元素的添加或删除操作

if __name__ == '__main__':
    from collections import deque
    deque= deque()
    # 从后面添加入队
    deque.append(2)
    deque.append(5)
    deque.append(4)
    # 从队列头入队
    deque.appendleft(3)
    deque.appendleft(1)
    print(deque)
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
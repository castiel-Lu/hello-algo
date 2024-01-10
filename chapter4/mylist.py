class MyList(object):

    def __init__(self):
        # 定义初始容量为10
        self._capacity: int = 10
        # 初始化一个长度为10，值都为0的数组用于存储
        self._arr: list[int] = [0] * self._capacity
        # 定义初始数字大小为0
        self._size: int = 0
        # 定义扩展率为2
        self._extend_ratio: int = 2


    def size(self) -> int:
        # 查询数组大小
        return self._size


    def capacity(self) -> int:
        # 查询数组的容量
        return self._capacity


    def get(self, index: int) -> int:
        # 如果查询的索引小于0或者大于数组的长度，报索引越界
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        # 返回目标索引处的值
        return self._arr[index]


    def set(self, num: int, index: int):
        # 如果设置索引处小于0或者大于数组的长度，报数组越界
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        # 设置数组的值
        self._arr[index] = num


    def add(self, num: int):
        # 如果数组已经达到容量大小了，需要扩容以满足新增需求
        if self._size == self._capacity:
            self.extend_capacity()
        # 在数组最后加上值num
        self._arr[self._size] = num
        # 数组大小+1
        self._size += 1


    def insert(self, index: int, num: int):
        # 如果要插入的索引小于0，或者大于数组的长度，报索引越界
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        # 如果当前数组已经满了，扩展数组的容量
        if self._size == self._capacity:
            self.extend_capacity()
        # 将index之后的数值往后挪一位
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        # 设置index位的值为num
        self._arr[index] = num
        # 数组的大小+1
        self._size += 1


    def remove(self, index: int):
        # 如果要删除的索引小于0或者大于数组的长度，报索引越界
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        # 将index索引所在位置的值保存下来
        num = self._arr[index]
        # 将index位之后的值都往前挪一位
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        # 数组的大小-1
        self._size -= 1
        # 返回删除的值
        return num


    def extend_capacity(self):
        # 将原数组扩大
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        # 设置容量大小为扩容后大小
        self._capacity = len(self._arr)


    def to_array(self) -> list[int]:
        # 返回有效长度的列表
        return self._arr[:self._size]
    
# 通过多次探测来处理哈希冲突，方式主要有线性探测、平方探测和多次哈希等
# 1. 线性探测
# 采用固定步长的线性搜索来进行探测
# 插入元素时通过哈希函数计算桶索引，当桶内已有元素，则从冲突位置向后线性遍历，直到找到空桶，将元素插入其中
# 查找元素时若发现哈希冲突，则使用相同步长向后进行线性遍历，直到找到对应元素，返回value即可；如果发现空桶，说明目标不在哈希表中，返回None

# 不能在开放寻址哈希表中直接删除元素，因为删除会在数组内产生一个空桶，在查询时会导致返回
# 解决这个问题可以采用懒删除机制，利用一个常量TOMBSTONE来标记这个桶，在该机制下，None和TOMBSTONE都代表空桶，都可以放置键值对，但是查询时找到TOMESTONE会继续遍历
# 懒删除可能会加速哈希表的性能退化，因为随着TOMBSTONE的增加，搜索时间会增加
# 为此考虑在线性探测中记录遇到的首个TOMBSTONE的索引，并将搜索到的目标元素与该TOMBSTONE交换位置，当每次查询或添加元素时，元素会被移动到距离理想位置更近的桶，从而优化查询效率

# 2. 平方探测
# 常用跳过探测次数的平方的步数，其优势为
#   通过跳过探测次数平方的距离，试图缓解线性探测的聚集效应
#   跳过更大的距离来寻找空位置，有助于数据分布得更加均匀
# 但是平方探测仍会存在聚集现象，且随着平方的增长，平方探测可能不会探测整个哈希表，意味着即便有空桶，平方探测也可能无法访问它

# 3.多次哈希
# 使用多个哈希函数进行探测，hash函数1出现冲突，尝试hash函数2，依此类推

# python是采用开放寻址方式上线哈希的，字典使用伪随机数进行探测

class Pair(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMapOpenAddressing(object):

    def __init__(self):
        # 键值对数量
        self.size = 0
        # 哈希表容量
        self.capacity = 4
        # 触发扩容的负载因子阈值
        self.load_thres = 2.0 / 3.0
        # 扩容倍数
        self.extend_ratio = 2
        # 桶数组
        self.buckets = [None] * self.capacity
        # 删除标记
        self.TOMBSTONE = Pair(-1, "-1")

    def hash_func(self, key):
        return key % self.capacity

    def load_factor(self):
        # 负载因子计算方式
        return self.size / self.capacity

    def find_bucket(self, key: int):
        index = self.hash_func(key)
        first_tombstone = -1
        # 当遇到空桶时跳出
        while self.buckets[index] is not None:
            # 当找到key时，返回对应的桶索引
            if self.buckets[index].key == key:
                # 如果之前遇到了删除标记，则将键值对移动至该索引处
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone
                return index
            # 遇到首个删除标记
            if first_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tombstone = index
            # 计算桶索引，越过尾部则返回头部，使用取余方式计算
            index = ( index + 1) % self.capacity
        # 若key不存在，则返回添加点的索引
        return index if first_tombstone == -1 else first_tombstone

    def get(self, key: int):
        index = self.find_bucket(key)
        # 当索引处不为None或者删除标记时返回索引处的值
        if self.buckets[index] is not [ None, self.TOMBSTONE ]:
            return self.buckets[index].value
        # 其他情况返回None
        return None

    def put(self, key, value):
        # 当负载因子超过阈值，执行扩容
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.find_bucket(key)
        # 如果找到键值对，则覆盖value并返回
        if self.buckets[index] not in [ None, self.TOMBSTONE ]:
            self.buckets[index].value = value
            return
        # 若键值对不存在，则添加该键值对
        self.buckets[index] = Pair(key, value)
        # 此时哈希表长度+1
        self.size += 1

    def remove(self, key: int):
        index = self.find_bucket(key)
        # 若找到键值对，则用删除标记覆盖它
        if self.buckets[index] not in [ None, self.TOMBSTONE ]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1

    def extend(self):
        # 暂存原哈希表
        buckets_tmp = self.buckets
        # 初始化新扩容的新哈希表
        self.capacity *= self.extend_ratio
        self.buckets= [None] * self.capacity
        self.size = 0
        for pair in buckets_tmp:
            # 如果非空，将值搬运至新哈希表
            if pair is not [None, self.TOMBSTONE]:
                self.put(pair.key, pair.value)

    def print(self):
        for pair in self.buckets:
            if pair is None:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(pair.key, "->", pair.value)
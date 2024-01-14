# 使用链式地址方式解决hash冲突问题
# 将单个元素转换为链表，将键值对作为链表节点，将所有发生冲突的键值对都存储在同一个链表中

# 操作方式的变化
# 查询：输入key，经过hash函数得到桶索引，即可访问链表头节点，然后遍历链表并对比key以查找目标键值对
# 添加：先通过hash函数访问链表头节点，然后将节点添加到链表中
# 删除：根据hash函数的结果访问链表头部，接着遍历链表以查找目标节点并将其删除

# 存在的局限性
# 占用空间增大
# 查询效率降低

class Pair(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

# 实现方法中使用列表代替链表，相当于多维数组；列表的动态扩容方法，当负载因子超过2/3时，将哈希表扩容至原先2倍
class HashMapChaining(object):
    def __init__(self):
        # 初始化长度为0
        self.size = 0
        # 初始化容量为4
        self.capacity = 4
        # 参照值
        self.load_thres = 2.0 / 3.0
        # 扩展率设置为2倍
        self.extend_ratio = 2
        # 初始化二维数组用于存储hash后的值
        self.buckets = [[] for _ in range(self.capacity)]

    def hash_func(self, key):
        # 简单的hash
        return key % self.capacity

    def load_factor(self):
        # 负载因子
        return self.size / self.capacity

    def get(self, key: int):
        # 计算key的索引
        index = self.hash_func(key)
        # 插入buckets内的对应数组
        bucket = self.buckets[index]
        # 因为hash冲突，某个hash值对应的数组内可能有多个值，这些需要遍历获取到需要的值
        for pair in bucket:
            if pair.key == key:
                return pair.value
        return None

    def put(self, key: int, value: int):
        # 如果负载因子大于2/3，扩容二维数组
        if self.load_factor() > self.load_thres:
            self.extend()
        # 计算hash索引
        index = self.hash_func(key)
        # 获取存储对应索引的数组
        bucket = self.buckets[index]
        # 开始遍历，遇到指定的key，更新其值value，并返回
        for pair in bucket:
            if pair.key == key:
                pair.value = value
                return
        # 若没有找到对应的key，则将键值对添加到尾部
        pair = Pair(key, value)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        # 获取key的hash值索引
        index = self.hash_func(key)
        # 取出对应索引的数组
        bucket = self.buckets[index]
        # 开始遍历，找到就删除这个键值对
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        # 获取当前的二维数组
        buckets = self.buckets
        # 扩大数组的容量，这时就是扩大2倍
        self.capacity *= self.extend_ratio
        # 生成新的空二维数组
        self.buckets = [[] for _ in range(self.capacity)]
        # 设置当前数组大小为0
        self.size = 0
        # 将之前的数组放入新创建的数组
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.value)

    def print(self):
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + "->" + pair.value)
            print(res)
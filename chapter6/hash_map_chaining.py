# 使用链式地址方式解决hash冲突问题
# 将单个元素转换为链表，将键值对作为链表节点，将所有发生冲突的键值对都存储在同一个链表中

# 操作方式的变化
# 查询：输入key，经过hash函数得到桶索引，即可访问链表头节点，然后遍历链表并对比key以查找目标键值对
# 添加：先通过hash函数访问链表头节点，然后将节点添加到链表中
# 删除：根据hash函数的结果访问链表头部，接着遍历链表以查找目标节点并将其删除

# 存在的局限性
# 占用空间增大
# 查询效率降低

# 实现方法中使用列表代替链表，相当于多维数组；列表的动态扩容方法，当负载因子超过2/3时，将哈希表扩容至原先2倍
class HashMapChaining(object):
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets = [[] for _ in range(self.capacity)]
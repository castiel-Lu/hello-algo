
class Pair(object):
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class ArrayHashMap(object):
    def __init__(self):
        # 初始化一个长100的空数组用于存储数据
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        # 简单的hash算法取余
        index = key % 100
        return index

    def get(self, key: int):
        index: int = self.hash_func(key)
        pair = self.buckets[index]
        if pair is None:
            return None
        return pair.value

    def put(self, key: int, value: str) -> None:
        # 创建Pair结构
        pair = Pair(key, value)
        # 对key进行hash，获取index
        index: int = self.hash_func(key)
        # 存入
        self.buckets[index] = pair

    def pop(self, key: int):
        # 获取索引
        index: int = self.hash_func(key)
        # 获取存的键值对
        pair = self.buckets[index]
        # 将值设置为None，表示删除
        self.buckets[index] = None
        return pair.value

    def entry_set(self) -> list[Pair]:
        result: list[Pair] = []
        # 遍历取出有效值
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result

    def key_set(self):
        result = []
        # 遍历取出有效值
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self):
        result = []
        # 遍历取出有效值
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.value)
        return result

    def print(self):
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.value)


if __name__ == '__main__':
    print("使用默认字典方式：")
    hmap = {}
    hmap[12836] = 'A'
    hmap[15937] = 'B'
    hmap[16750] = 'C'
    hmap[13276] = 'D'
    hmap[10583] = 'E'
    print("初始化的hash表内容：{}".format(hmap))
    name: str = hmap[15937]
    print("查询某个值：{}".format(name))
    delete = hmap.pop(10583)
    print("删除某个值：{}".format(delete))
    for key, value in hmap.items():
        print("items元素遍历打印：", key, "->", value)
    for key in hmap.keys():
        print("key值遍历打印：", key)
    for value in hmap.values():
        print("value值遍历打印：",value)

    print()
    print("基于数组的hashmap：")
    hmap1 = ArrayHashMap()
    hmap1.put(12836, "A")
    hmap1.put(15937, "B")
    hmap1.put(16750, "C")
    hmap1.put(13276, "D")
    hmap1.put(10583, "E")
    print("初始化的hash表内容：{}".format(hmap1))
    name = hmap1.get(15937)
    print("查询某个值：{}".format(name))
    delete = hmap1.pop(10583)
    print("删除某个值：{}".format(delete))
    for pair in hmap1.entry_set():
        print("items元素遍历打印：", pair.key, "->", pair.value)
    for key in hmap1.key_set():
        print("key值遍历打印：", key)
    for value in hmap1.value_set():
        print("value值遍历打印：",value)
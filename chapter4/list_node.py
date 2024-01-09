# 双向链表
class ListNode(object):
    def __init__(self, val: int):
        self.val = val
        self.next: ListNode = None
        self.prev: ListNode = None


def insert(n0: ListNode, p: ListNode, reverse=False):
    # 如果是往前插入的
    if reverse:
        # 取一个中间值nx保存n0前一个节点的值，可能是None
        nx = n0.prev
        # 设置插入的p的下一个节点为n0
        p.next = n0
        # 设置p的上一个节点为保存的状态nx
        p.prev = nx
        # 设置n0的上一个节点为p
        n0.prev = p
        # 如果nx不是None，就不要设置它的下一个节点是什么了
        if nx is not None:
            nx.next = p
    else:
        # n1记录n0的下一个节点状态
        n1 = n0.next
        # 要插入的P节点的下一个节点设置为n1
        p.next = n1
        # n0的下一个节点设置为P
        n0.next = p
        # 插入的P节点的上一个节点设置为n0
        p.prev = n0
        # 原来n0的下一个节点，它所记录的上一个节点是n0，现在改为P节点
        # 如果n1没有下一个节点，就不用记录它的前一个节点是什么了
        if n1 is not None:
            n1.prev = p


def remove(n0: ListNode):
    # 如果n0的前一个节点是None，那么n0是第一个节点
    # 那么就将n0的下一个节点的prev设置为None就行了
    if not n0.prev:
        n1 = n0.next
        n1.prev = None
        return

    # 如果n0的下一个节点是None，那么n0是尾节点
    # 那么将n0前面一个节点的next设置为None即可
    if not n0.next:
        n1 = n0.prev
        n1.next = None
        return

    # 如果n0是中间的节点
    # n1是n0后一个节点，P是n0前一个节点
    # 则设置n1的前一个节点为P
    # 设置P的后一个节点为n1即可
    n1 = n0.next
    p = n0.prev
    p.next = n1
    n1.prev = p


def access(head: ListNode, index: int) -> ListNode:
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head


if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(5)
    n3 = ListNode(2)
    n4 = ListNode(4)
    n0.prev = None
    n0.next = n1
    n1.prev = n0
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3
    n4.next = None

    # 查找
    node = access(n0, 3)
    # 打印n0后3个的节点的值，即n3
    print("n0后3个节点的值为{}".format(node.val))
    # 打印n0后4个的节点的值，即n4
    print("n0后4个节点的值为{}".format(node.next.val))
    # 打印n0后2个的节点的值，即n2
    print("n0后2个节点的值为{}".format(node.prev.val))

    # 插入n
    print("末尾插入前")
    nx = ListNode(100)
    # 先看下n1及其前后的值(n0和n2)
    print("n4的值为{}".format(n4.val))
    print("n4前一个节点的值，这里是n3为{}".format(n4.prev.val))
    print("n4后一个节点的值，这里是None为{}".format(n4.next))

    # 在n1后插入nx
    insert(n4,nx)
    print("末尾插入后")
    # 在看下n1及其前后的值(n0和nx)
    print("n4的值为{}".format(n4.val))
    print("n4前一个节点的值，这里是n3为{}".format(n4.prev.val))
    print("n4后一个节点的值，这里是nx为{}".format(n4.next.val))
    # print("n2前一个节点的值，这里是nx为{}".format(n2.prev.val))

    # 删除nx
    print("删除末尾插入的nx")
    remove(nx)
    print("n4的值为{}".format(n4.val))
    # print("n4前一个节点的值，这里是n0为{}".format(n1.prev.val))
    print("n4后一个节点的值，这里是None为{}".format(n4.next))

    # 往n0前插入nx
    insert(n0,nx,reverse=True)
    print("在n0前插入值后")
    # 在看下n0及其前后的值(n0和nx)
    print("n0的值为{}".format(n0.val))
    print("n0前一个节点的值，这里是nx为{}".format(n0.prev.val))
    print("n0后一个节点的值，这里是n1为{}".format(n0.next.val))
    print("nx前一个节点的值，这里是None为{}".format(nx.prev))

    remove(nx)

    # 往n4前插入nx
    insert(n4,nx,reverse=True)
    print("在n4前插入值nx后")
    # 在看下n0及其前后的值(n0和nx)
    print("n4的值为{}".format(n4.val))
    print("n4前一个节点的值，这里是nx为{}".format(n4.prev.val))
    print("n4后一个节点的值，这里是None为{}".format(n4.next))
    print("nx前一个节点的值，这里是n3为{}".format(nx.prev.val))
    print("nx后一个节点的值，这里是n4为{}".format(nx.next.val))
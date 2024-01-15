from collections import deque

class TreeNode(object):
    def __init__(self, val: int):
        # 节点值
        self.val = val
        # 左子节点
        self.left = None
        # 右子节点
        self.right = None

def list_to_tree_dfs(arr,i):
    if i < 0 or i >=len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = list_to_tree_dfs(arr, 2*i+1)
    root.right = list_to_tree_dfs(arr, 2*i+2)
    return root

def list_to_tree(arr):
    return list_to_tree_dfs(arr,0)
def level_order(root: TreeNode) -> list:
    # 层序遍历
    # 初始化队列
    queue = deque()
    # 加入根节点
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        # 队列出队
        node = queue.popleft()
        # 保留节点值
        res.append(node.val)
        # 左子节点入队
        if node.left is not None:
            queue.append(node.left)
        # 右子节点入队
        if node.right is not None:
            queue.append(node.right)
        return res

def pre_order(root: TreeNode):
    # 前序遍历
    if root is None:
        return
    # 访问优先级： 根节点->左子树->右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

def in_order(root: TreeNode):
    # 中序遍历
    if root is None:
        return
    # 访问优先级：左子树->根节点->右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root: TreeNode):
    # 后序遍历
    if root is None:
        return
    # 访问优先级：左子树->右子树->根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)

if __name__ == '__main__':
    root = list_to_tree(arr=[1,2,3,4,5,6,7])
    res = []
    pre_order(root)
    print(res)

    res.clear()
    in_order(root)
    print(res)

    res.clear()
    post_order(root)
    print(res)
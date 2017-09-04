
# 参考资料
# https://github.com/taizilongxu/interview_python
# https://sagittariusyx.github.io/2016/07/22/Python-binary-tree-traverse/
# 14 二叉树节点
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

# 15 层次遍历
# 层次遍历和先序遍历有联系，将queue换成stack，节点访问顺序左右调换即是先序遍历
def lookup(root):
    queue = [root]
    while queue:
        # print([n.data for n in queue])
        current = queue.pop(0) #队列pop队头
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        yield current.data

# 16 深度遍历/先序遍历
def deep_recur(root):
    output = []
    def deep(root):
        if root == None:
            return
        output.append(root.data)
        deep(root.left)
        deep(root.right)
    deep(root)
    return output

## 先序遍历非递归
def deep_iter(root):
    if root == None:
        return
    node = root
    stack = []
    output = []
    while node or stack:
        while node:
            output.append(node.data)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return output

# 中序遍历
def order_search(root):
    output = []
    def order(root):
        if root == None:
            return
        order(root.left)
        output.append(root.data)
        order(root.right)
    order(root)
    return output

## 中序遍历非递归
# 在先序遍历的基础上改节点访问位置
def order_iter(root):
    if root == None:
        return
    node = root
    stack = []
    output = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        output.append(node.data)
        node = node.right
    return output

# 后序遍历
def postorder_search(root):
    output = []
    def postorder(root):
        if root == None:
            return
        postorder(root.left)
        postorder(root.right)
        output.append(root.data)
    postorder(root)
    return output

## 后序遍历非递归
# 后序遍历较复杂，
def postorder_iter(root):
    if root == None:
        return
    node = root
    stack = [root]
    output = []
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        output.append(node.data)
    output.reverse() # 注意不能写成output = output.reverse()
    return output

if __name__ == '__main__':
    print("-------preorder-------")
    result11 = list(deep_recur(tree))
    print(result11)
    result12 = list(deep_iter(tree))
    print(result12)
    print('--------order---------')
    result21 = order_search(tree)
    print(result21)
    result22 = order_iter(tree)
    print(result22)
    print('--------postorder-------')
    result31 = postorder_search(tree)
    print(result31)
    result32 = postorder_iter(tree)
    print(result32)
    print('---------------')
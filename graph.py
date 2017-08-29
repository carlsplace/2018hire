# 20180825 阿里笔试
# 求邻接表表示的无向图中子图的个数

# http://www.dannysite.com/blog/232/
def dfs(graph, node):
    """
    深度优先搜索
    graph是邻接表表示的图
    """
 
    # searched 用于存放已探索的节点
    # query_queue 是用来存放待探索节点的 to-do 列表，并将其模拟成 LIFO
    searched, query_queue = set(), []
 
    # 最初，to-do 列表中只有遍历的起点
    query_queue.append(node)
 
    while query_queue:
        # 总是从 to-do 列表的最后弹出一个待探索的节点
        q_node = query_queue.pop()
 
        if q_node in searched:
            continue
 
        searched.add(q_node)
 
        for neighbor in graph[q_node]:
            # 将邻居节点推入 to-do 列表
            query_queue.append(neighbor)
 
        yield q_node


from collections import deque
def bfs(graph, node):
    """
    广度优先搜索
    """
 
    # parents 记录所有可达节点与对应的父节点，这里是一个字典，我们将其 可达节点 作为 key，而将其 父节点 作为 value
    # query_queue 是用来存放待探索节点的 to-do 列表，这里是一个 FIFO
    parents, query_queue = {node: None}, deque([node])
 
    while query_queue:
        # 总是从 FIFO 的左侧弹出待探索的节点
        q_node = query_queue.popleft()
 
        for neighbor in graph[q_node]:
            if neighbor in parents:
                continue
 
            # 记录探索到的邻居节点及其父节点
            parents[neighbor] = q_node
 
            # 将其邻居节点推入 to-do 列表
            query_queue.append(neighbor)

        yield q_node
    # return parents

if __name__ == "__main__":
    graph = [[1,2,4],
             [0,2],
             [0,1,3,5],
             [4,5],
             [0,3],
             [3,6],
             [5],
             [8,9],
             [7],
             [7],
             [11],
             [10],
             []]
    
    # 子图查找
    nodes = set(range(len(graph)))
    count = 0
    while nodes:
        start = nodes.pop()
        nodes.add(start)
        searched = bfs(graph, start)
        for node in searched:
            nodes.remove(node)
        count += 1

    print(count)
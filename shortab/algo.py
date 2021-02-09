import math
def compute(graph):
    for a in range(0,len(graph)):
        for b in range(0,len(graph)):
            for c in range(0,len(graph)):
                graph[b][c] = min(graph[b][c],graph[b][a] + graph[a][c])
    return graph 

def tests(graph,vertex):
    try:
        li = graph.split('\r\n')
        output = []
        for item in li:
            val = item.split(' ')
            n=[]
            for item in val:
                if item=='-':
                    n.append(math.inf)
                    continue
                n.append(int(item))
            output.append(n)
        return output
    except Exception as e:
        return 0

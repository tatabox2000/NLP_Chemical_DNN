import  numpy as np
import seaborn
import pylab as plt
import networkx as nx
import math
import pandas as pd
import community

def eigenvalue():
    A = np.array([
                  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]

    ])

    index = np.arange(1,A.shape[0]+1,1)
    df = pd.DataFrame(A,index=index,columns=index)
    seaborn.heatmap(A)
    plt.show()
    print(df)
    la, v = np.linalg.eig(A)
    #print(la,v)
    print(la)
    #v = np.array([v[2],v[1]])

    print(v,'connect')
    result = A *v[2]
    #print(result)
    seaborn.heatmap(result)
    plt.show()
    Graph = nx.Graph()

    for i ,col in enumerate(df.columns) :
        names = np.repeat(df.index[i],df.index.shape[0])
        pair = list(zip(names, df.index, df[col]))
        result = []
        node1 = []
        node2 = []
        for j, a in enumerate(pair):
                node1.append(a[0])
                node2.append(a[1])
                weight = float(a[2]) * 30
                if weight == 0.0:
                    pass
                else:
                    result.append((a[0], a[1], weight))
        node1 = set(node1)
        node2 = set(node2)
        nodes = list(node2 | node1)
        Graph.add_nodes_from(nodes)
        Graph.add_weighted_edges_from(result)
    partition =community.best_partition(Graph)
    pos = nx.spring_layout(Graph,k=0.5)
    color_list=['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
    for cluster in set(partition.values()):
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes]==cluster]
        if cluster > 10:
            color ='C9'
        else:
            color =color_list[cluster]
        nx.draw_networkx_nodes(Graph,pos,list_nodes,node_size=(cluster+1)*200,node_color=color)
        nx.draw_networkx_labels(Graph, pos)
        nx.draw_networkx_edges(Graph,pos)
    plt.show()
    print(result)
    nx.write_gexf(Graph, "test_matrix.gexf")

    #print(la,v)
if __name__ == '__main__':
    eigenvalue()
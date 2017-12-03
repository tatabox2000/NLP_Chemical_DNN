import pandas as pd
import numpy as np
from numpy import nan

def make_network():
    import networkx as nx
    import math
    import collections

    df = pd.read_csv('.\\Data\\MACCSKeys_tanimoto.csv',index_col='CAS')
    Graph = nx.Graph()
    #Graph.add_nodes_from(df.index)
    edges = []
    df = df.replace('None',0)
    df = df.fillna(0)
    for i ,col in enumerate(df.columns) :
        columns = np.repeat(col,df.index.shape[0])
        pair = list(zip(columns,df.index,df[col]))
        result = []
        node1=[]
        node2=[]
        for j,a in enumerate(pair):
            if a[2]==0:
                pass
            elif a[2] is np.nan:
                print('remove nan')
            elif float(a[2])<0.7:
                pass
            elif float(a[2]) == 1:
                pass
            else:
                #print(a)
                node1.append(a[0])
                node2.append(a[1])
                result.append(a)
        node1= set(node1)
        node2 = set(node2)
        nodes = list(node2 | node1)
        Graph.add_nodes_from(nodes)
        Graph.add_weighted_edges_from(result)
    # #print(Graph.edges(data=True))
    nx.write_gexf(Graph, "tanimoto_.gexf")

if __name__ == '__main__':
    make_network()
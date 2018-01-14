import pandas as pd
import numpy as np
from numpy import nan

def make_network():
    import networkx as nx
    import math

    df = pd.read_csv('.\\Data\\MACCSKeys_tanimoto.csv',index_col='CAS')
    df2 = pd.read_csv('connect_result.csv',index_col='CAS')
    df2['names'] = df2['tox_median'].astype(str)+'_'+df2['iupac_name']
    # print(df2['tox_median'].shape)
    # print(df2['iupac_name'].shape)
    # print(df['names'].shape)
    # print(df.columns.shape)
    # print(df.columns[0])
    # print(df.columns,df2.index)
    # print(df.columns.shape,df2.index.shape)
    Graph = nx.Graph()
    #Graph.add_nodes_from(df.index)
    edges = []
    df = df.replace('None',0)
    df = df.fillna(0)
    for i ,col in enumerate(df.columns) :
        print(i)
        columns = np.repeat(df2['names'][i],df.index.shape[0])
        pair = list(zip(columns,df2['names'],df[col]))
        result = []
        node1=[]
        node2=[]
        for j,a in enumerate(pair):
            if a[2]==0:
                pass
            elif a[2] is np.nan:
                print('remove nan1')
            elif a[0] is np.nan:
                print('remove nan2')
            elif a[1] is np.nan:
                print('remove nan3')
            elif float(a[2])<0.7:
                pass
            elif float(a[2]) == 1:
                pass
            else:
                #print(a)
                node1.append(a[0])
                node2.append(a[1])
                weight = float(a[2]) *30
                if weight == 0.0:
                    pass
                else:
                    result.append((a[0],a[1],weight))
        node1= set(node1)
        node2 = set(node2)
        Graph.add_nodes_from(nodes)
        Graph.add_weighted_edges_from(result)
    # #print(Graph.edges(data=True))
    # nx.write_gexf(Graph, "tanimoto_.gexf")

if __name__ == '__main__':
    make_network()
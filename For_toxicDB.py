import pandas as pd
import networkx as nx
import collections
import matplotlib.pyplot as plt
import  numpy as np
import  seaborn as sns

def read_and_change():
    df = pd.read_csv('toxic_DB2.csv')
    name_col = 1
    #target_col1 = 8
    target_col1 = 8
    target_col2 = 24
    #target_col2 = None
    target_col3 = None

    #df.iloc[:, [1]] = df.iloc[:,[1]].astype('str')+' '+df.iloc[:,[0]].astype('str')
    df['化学物質名'] = df['化学物質名'].astype( 'str')+'_'+ df['CAS'].astype('str')
    df.iloc[:, [6]] = df.columns[6]+' '+df.iloc[:,[6]].astype('str')
    #df.iloc[:, [5]] = df.columns[5]+' '+df.iloc[:,[5]].astype('str')

    df['category'] = df.iloc[:,5]
    bool1 = (df.iloc[:,5]>10000) & (df.iloc[:,5]<=1000000)
    df.loc[bool1, 'category'] = 'A'
    bool1 = (df.iloc[:,5]>100) & (df.iloc[:,5]<=10000)
    df.loc[bool1, 'category'] = 'B'
    bool1 = (df.iloc[:,5]>0) & (df.iloc[:,5]<=100)
    df.loc[bool1, 'category'] = 'C'
    bool1 = (df.iloc[:,5]>0.01) & (df.iloc[:,5]<=0)
    df.loc[bool1, 'category'] = 'D'
    bool1 = (df.iloc[:,5]>0.0001) & (df.iloc[:,5]<=0.01)
    df.loc[bool1, 'category'] = 'E'
    bool1 = (df.iloc[:,5]>0.0000001) & (df.iloc[:,5]<=0.0001)
    df.loc[bool1, 'category'] = 'F'

    df.to_csv('ex.csv')

    Graph = nx.Graph()
    #Graph = nx.DiGraph()
    Graph.add_nodes_from(df.iloc[:,name_col].unique())
    edges = []
    for i in [target_col1,target_col2,target_col3]:
        if i == None:
            pass
        else:
            Graph.add_nodes_from(df.iloc[:,i].unique())
            pair = list(zip(df.iloc[:,name_col].astype('str'),df.iloc[:,i].astype('str')))

            count_dict = collections.Counter(pair)
            max_pair = count_dict.most_common(1)
            max_count = max_pair[0][1]

            for k , v in count_dict.items():
                weight = v/max_count
                b = (k[0],k[1],weight)
                edges.append(b)
    Graph.add_weighted_edges_from(edges)
    #print(Graph.edges(data=True))
    nx.write_gexf(Graph, "toxic_and_fish.gexf")

def read_hestplot():
    df = pd.read_csv('toxic_DB2.csv')
    data = df.iloc[:,5]
    print(data.max())
    plt.hist(data,bins=np.logspace( -5,5, 500))
    plt.xscale("log")
    plt.show()

def read_deth_or_live_plot():
    df = pd.read_csv('toxic_DB2.csv')
    data = df.iloc[:,[4,5]]
    data['category'] = ''
    bool1 = (data.iloc[:,1]>10000) & (data.iloc[:,1]<=1000000)
    data.loc[bool1, 'category'] = 'A'
    # bool1 = (data.iloc[:,1]>100) & (data.iloc[:,1]<=10000)
    # data.loc[bool1, 'category'] = 'B'
    # bool1 = (data.iloc[:,1]>0) & (data.iloc[:,1]<=100)
    # data.loc[bool1, 'category'] = 'C'
    # bool1 = (data.iloc[:,1]>0.01) & (data.iloc[:,1]<=0)
    # data.loc[bool1, 'category'] = 'D'
    # bool1 = (data.iloc[:,1]>0.0001) & (data.iloc[:,1]<=0.01)
    # data.loc[bool1, 'category'] = 'E'
    # bool1 = (data.iloc[:,1]>0.0000001) & (data.iloc[:,1]<=0.0001)
    # data.loc[bool1, 'category'] = 'F'
    #
    # print(data)

    # data = data.replace('.*生存.*',1,regex = True)
    # data = data.replace('.*死亡.*',2,regex = True)
    #
    # data = data.replace('\D',0,regex = True)
    # data = data.dropna()

    # print(data.iloc[:,0].unique())
    # print(data)
    # plt.scatter(x = data.iloc[:,1],y = data.iloc[:,0])
    #
    # #data.plot(kind='scatter',x =data.iloc[:,1],y =data.iloc[:,0] )
    # plt.show()

    #sns.set(font='Yu Gothic')
    #sns.regplot(x = data.iloc[:,1],y = data.iloc[:,0])
    #plt.hist(data,bins=np.logspace( -5,5, 500))
    #plt.xscale("log")

if __name__ == '__main__':
    df = read_and_change()
    #read_hestplot()
    #read_deth_or_live_plot()


import time
import warnings

import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice

np.random.seed(0)
import  pandas as pd
import seaborn as sns

def coor_csv2cluster(n = 500):
    #test = np.random.rand(n,n)
    # lam = 0.1
    # test = np.random.exponential(1. / lam, size=n)
    # test = np.random.f(30,30,n)
    # test = test/test.max()
    # test = 1 - test
    # plt.subplot(3,1,1)
    # plt.hist(test,100)
    # test = np.triu(test,k=1)
    # df = pd.DataFrame(test)
    df2 = pd.read_csv('MACCSKeys_tanimoto.csv',skiprows=1,header=None)
    n = df2.shape[0]
    print(n)
    df2 = df2.replace('None',0)
    df2 = df2.fillna(0)
    df2 = df2.where(df2.notnull(), 0)
    index = df2.iloc[:,0]
    df = df2.drop(0,axis=1)
    df = df.iloc[:n,:n]
    df = df.astype('float')

    df[df == 1] = 0

    # for i,chack in enumerate(df.isnull().any()):
    #     if chack == True:
    #         print(i,chack)
    #     else:
    #         pass

    #df[df >0.8] = 1
    # df[(df > 0.6) & (df <= 0.75)] = 0.0
    # df[(df > 0.4) & (df <= 0.6)] = 0.0
    # df[(df > 0.2) & (df <= 0.4)] = 0.0
    # df[df <0.2] = 0

    for i in np.arange(0,n,1):
        for j in np.arange(0,n,1):
            if i == j:
                break
            else:
                df.iat[i,j] = df.iat[j,i]
    plt.subplot(3,1,2)

    sns.heatmap(df, fmt='g',cmap = "coolwarm")
    #sns.heatmap(df)


    spectral = cluster.SpectralClustering(
        n_clusters=50, eigen_solver='arpack',
        affinity='precomputed')
    result = spectral.fit(df)
    y_pred = result.labels_.astype(np.int)
    df2= pd.DataFrame(y_pred)
    df3 = df2.sort_values(by=[0],ascending=True)
    index= index.iloc[df3.index]
    print(index.iloc[df3.index])
    df = df.iloc[:,df3.index]
    df = df.iloc[df3.index,:]
    df = df.set_index(index)
    df.columns = index
    print(df3.index)

    plt.subplot(3,1,3)
    sns.heatmap(df, fmt='g',cmap="coolwarm")
    df3 = df3.set_index(index)
    df['cluster'] = df3
    #sns.heatmap(df)
    save_df = df['cluster']

    save_df.to_csv('tanimoto_cluster.csv')

    plt.show()

def connect_result():
    df1 = pd.read_csv('tanimoto_cluster.csv',header=None)
    df1 = df1.set_index(df1[0])
    df2 = pd.read_csv('connect_result.csv',index_col='CAS')
    df3 = pd.concat([df1, df2], axis=1)
    df3 = df3.rename(columns={1 : 'cluster'})
    df3 = df3.drop(0,axis=1)
    print(df1.head(),df2.head(),df3)
    df3.to_csv('cluster_name_and_tox_val.csv')

if __name__ == '__main__':
    coor_csv2cluster()
    connect_result()
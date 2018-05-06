#! env python
# -*- coding: utf-8 -*-

import os
import sys
import  pandas as pd
from sklearn.cluster import KMeans
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from IPython.display import SVG
from rdkit.Chem import Draw
from rdkit import rdBase
import skfuzzy as fuzz
import numpy as np

class clustering(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')

    def calcKmeans(self,name):
        os.chdir("C:\\googledrive\\Data\\tox_predict\\result\\fingerprint")
        data = pd.read_csv(name).fillna(0)
        values = data.drop(['CAS', 'name','canonical_smiles','tox_median'], axis=1).values
        kmeans = KMeans(n_clusters=30, random_state=0).fit(values)
        kmeans.labels_
        kmeans.cluster_centers_
        names = data[['CAS', 'name','canonical_smiles','tox_median']]
        names['cluster'] = kmeans.labels_
        #names.to_csv("kmeans.csv")
        return names
    def calkFussyMean(self,name):
        os.chdir("C:\\googledrive\\Data\\tox_predict\\result\\fingerprint")
        data = pd.read_csv(name).fillna(0)
        values = data.drop(['CAS', 'name','canonical_smiles','tox_median'], axis=1).values
        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
            values.T, 30, 2, error=0.005, maxiter=1000, init=None)
        columns = np.arange(0,len(u0[0]),1)
        index = np.arange(0,len(u0),1)
        df = pd.DataFrame(u0,columns=columns,index=index).T
        names = data[['CAS', 'name','canonical_smiles','tox_median']]
        result = pd.merge(names,df,left_index=True,right_index=True)
        result = result.set_index("CAS")
        result.to_csv("fuzzy.csv")
        return result

    def makePictures(self,result_df,multi=None):
        dir_list = result_df['cluster'].unique()
        try:
            os.makedirs('pics')
        except:
            pass
        os.chdir('.\\pics')
        for dir in dir_list:
            dir = str(dir)
            try:
                os.makedirs(dir)
            except:
                pass
        extract = zip(result_df['CAS'], result_df['canonical_smiles'], result_df['cluster'], result_df['tox_median'])

        for CAS, smiles, cluster, tox_median in extract:
            try:
                m = Chem.MolFromSmiles(smiles)
                AllChem.Compute2DCoords(m)
                name = '.\\' + str(cluster) + '\\' +str(tox_median) +'__' + str(CAS) + '.png'
                #if str(tox_median) == 'nan':
                    #print(name)
                Draw.MolToFile(m, name)
            except:
                #     print("pass1")
                pass

if __name__ == '__main__':
    cl = clustering()
    name = "C:\\googledrive\\Data\\tox_predict\\result\\fingerprint\\MACCSKeys.csv"
    #df = cl.calcKmeans(name)
    df = cl.calkFussyMean(name)
    #cl.makePictures(df)

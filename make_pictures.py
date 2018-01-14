from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.Draw import IPythonConsole
from IPython.display import SVG
from rdkit.Chem import Draw
from rdkit import rdBase
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolDescriptors
from rdkit import DataStructs
import pandas as pd
import numpy as np
import math
import os
import pylab as plt

os.chdir('C:\\Users\\tatab\\OneDrive\\NLP')
def make_pictures(multi = None):
    result_df = pd.read_csv('cluster_name_and_tox_val.csv',dtype={'tox_median':'float'},sep=',')
    #result_df =result_df.set_index('CAS')
    print(result_df.index)
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
    extract = zip(result_df['CAS'],result_df['canonical_smiles'],result_df['cluster'],result_df['tox_median'])
    #print(result_df.loc['29082-74-4'])
    for CAS,smiles,cluster,tox_median in extract:
        try:
            m = Chem.MolFromSmiles(smiles)
            AllChem.Compute2DCoords(m)
            name = '.\\' + str(cluster) + '\\' +str(tox_median)+'__'+ str(CAS) + '.png'
            #print(name)
            if str(tox_median) == 'nan':
                print(name)
            Draw.MolToFile(m, name)
        except:
            pass
def cluster_var_hist():
    df = pd.read_csv('cluster_name_and_tox_val.csv')
    result_df = df.set_index(df['CAS'])
    cluster_list = result_df['cluster'].unique()
    os.chdir('C:\\Users\\tatab\\OneDrive\\NLP\pics')
    for cluster in cluster_list:
    #for i in np.arange(1,2,1):
        #cluster = i
        #print(cluster)
        calc_df = result_df[result_df['cluster'].isin([cluster])]
        y = calc_df['tox_median']
        #print(calc_df['tox_median'],calc_df['cluster'])
        try:
            plt.figure()
            plt.hist(y,bins=30)
            #calc_df.plot(y=['tox_median'],bins=50,kind = 'hist')
            plt.title('tox value histgram')
            plt.ylabel('count')
            plt.xlabel('tox value')
            #name = '.\\' + str(cluster) + '\\' + str(cluster) + '__' + 'histgram.png'
            name = str(cluster) + '__' + 'histgram.png'
            print(name)
            plt.savefig(name)
            #plt.show()
        except:
            print(cluster)
            print('cant')
            pass
if __name__ == '__main__':
    #make_pictures()
    cluster_var_hist()
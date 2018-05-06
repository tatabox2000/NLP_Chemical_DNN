import numpy as np
import pandas as pd
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

def calc_bit(df):
    print()
    fin1= np.array(list(df['cactvs_fingerprint'][0]))
    fin2 = np.array(list(df['cactvs_fingerprint'][1]))
    print(fin1,fin2)

    result = DataStructs.FingerprintSimilarity(fin1,fin2)
    print(result)

    num =list('0101001001010101011111')
    print(num)
    array = np.array(num)
    print(array)


if __name__ == '__main__':
    df = pd.read_csv('C:\\Users\\admin\\OneDrive\\NLP\\connect_result.csv',dtype={'cactvs_fingerprint':'object'})
    calc_bit(df)
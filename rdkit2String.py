#! env python
# -*- coding: utf-8 -*-

import os
import sys
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
import pubchempy as pcp
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem import MACCSkeys
from rdkit.Chem import AllChem
class rdkit2String(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')

    def main(self):
        os.chdir("C:\\googledrive\\Data\\tox_predict\\result\\fingerprint")
        baseCSV = "C:\\googledrive\\Data\\tox_predict\\cluster_name_and_tox_val.csv"
        baseDf = pd.read_csv(baseCSV)
        resultDf = pd.DataFrame(columns=np.arange(0,166,1))
        resultDf['name'] = []
        resultDf['CAS'] = []
        resultDf['canonical_smiles'] =[]
        i = 0
        for i in np.arange(0,len(baseDf.index),1):
            print(i)
            name = baseDf['iupac_name'][i]
            inchi1 = baseDf['inchi'][i]
            cas = baseDf['CAS'][i]
            smiles = baseDf['canonical_smiles'][i]
            toxValue = baseDf['tox_median'][i]
            #inchi2 = baseDf['standard_inchi'][100]
            try:
                mol1 = Chem.MolFromInchi(inchi1)
                #mol2 = Chem.MolFromInchi(inchi2)
                fgp1 = MACCSkeys.GenMACCSKeys(mol1)
                value = [1]*len(tuple(fgp1.GetOnBits()))
                tempDf = pd.DataFrame([value],columns=list(fgp1.GetOnBits()))
                tempDf["name"] = name
                tempDf['CAS'] = cas
                tempDf['canonical_smiles']=smiles
                tempDf['tox_median']=toxValue
                resultDf =resultDf.append(tempDf)
            except:
                pass
        resultDf = resultDf.set_index('CAS')
        resultDf.to_csv("MACCSKeys.csv")

if __name__ == '__main__':
    rd = rdkit2String()
    rd.main()

#! env python
# -*- coding: utf-8 -*-

import os
import sys
import pickle
import pandas as pd
import os
import numpy as np
from pubchempy import Compound, get_compounds
import re
import pubchempy as pcp

class Iupac2CASorSmiles(object):
    def __init__(self):
        self.__ROOT = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.__EXE_PATH = sys.executable
        self.__ENV_PATH = os.path.dirname(self.__EXE_PATH)
        self.__LOG = os.path.join(self.__ENV_PATH, 'log')

    def getCasFromInchi(self,inchi):
        cas_rns = []
        cid_list = pcp.get_compounds(inchi, 'inchi')
        #iupacName
        cas_rns.append(cid_list[0].iupac_name)
        #cas_rns.append(inchi)
        #isomericSmile
        cas_rns.append(cid_list[0].isomeric_smiles)
        results = pcp.get_synonyms(cid_list[0].cid, 'cid')
        for result in results:
            for syn in result.get('Synonym', []):
                match = re.match('(\d{2,7}-\d\d-\d)', syn)
                if match:
                    cas_rns.append(match.group(1))
        return cas_rns

    def iupacName2Cas(self,saveFile = None):
        baseCSV = "C:\\googledrive\\Data\\tox_predict\\chemble\\small_ver.csv"
        #baseCSV = "C:\\googledrive\\Data\\tox_predict\\chemble\\test.csv"
        baseDf = pd.read_csv(baseCSV)
        baseDF = baseDf[["molregno","standard_inchi"]]
        columns = ["molregno","standard-inchi","IUPAC-Name","isomeric-smiles","CAS", "CAS2", "CAS3", "CAS4", "CAS5", "CAS6", "CAS7", "CAS8"]
        if os.path.exists(str(saveFile)) == True:
            chackDf = pickle.load(open('save.pickle', mode='w'))
        else:
            chackDf = pd.DataFrame(columns= columns)

        for i in np.arange(0,len(baseDf.index),1):
            inchi = baseDF['standard_inchi'].iloc[i]
            nameCas = self.getCasFromInchi(inchi)
            #nameCas.insert(0, df["molregno"].iloc[i])
            #nameCas.insert(1, df['standard_inchi'].iloc[i])
            temp = baseDF.iloc[i]
            temp = temp.values.tolist()
            temp = temp+nameCas
            #print(temp)
            if temp == None:
                print("None")
            else:
                try:
                    columnsTemp = columns[0:len(temp)]
                    tempDf  = pd.DataFrame([temp],columns=columnsTemp)
                    chackDf = chackDf.append(tempDf)
                    print(i)
                except:
                    print("pass")

if __name__ == '__main__':
    i2CorS = Iupac2CASorSmiles
    i2CorS.iupacName2Cas

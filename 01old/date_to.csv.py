import pandas as pd
import numpy as np
import re
import cirpy

def date_to_CAS():
    df = pd.read_csv('connect_result.csv')
    df2 = pd.read_csv('.\\Data\\toxic_DB2.csv')
    #print(df2.head(5))
    #print(df.head())
    CAS_numbers = []
    iupac_names = []
    old_CAS =[]
    pairs = zip(df2['CAS'],df2['化学物質名'])
    for i,name in enumerate(pairs):
        #print(name[0])
        m = re.search('\/',name[0])
        if m ==None:
            pass
        else:
            if old_CAS == []:
                dst = re.sub('\/', '-', name[0])
                iupac_names.append(name[1])
                CAS_numbers.append(dst)
                old_CAS.append(name[0])
            else:
                if old_CAS[len(old_CAS)-1] is not name[0]:
                    dst = re.sub('\/','-',name[0])
                    iupac_names.append(name[1])
                    CAS_numbers.append(dst)
                    old_CAS.append(name[0])
                else:
                    pass
            #print(m)
    names = pd.DataFrame({'iupac_names':iupac_names,'CAS_numbers':CAS_numbers,'old_CAS':old_CAS})
    names = names.set_index('CAS_numbers')
    names.to_csv('names.csv')
    for CAS in CAS_numbers:
        print(CAS)
    print(len(CAS_numbers))

def name_to_cas():
    df = pd.read_csv('names.csv')
    CAS = []
    for iupac_name in df['iupac_names']:
        CAS_result = cirpy.resolve(iupac_name, 'cas')
        CAS.append(CAS_result)
        print(iupac_name)
    df['CAS_from_DB_'] = CAS
    df.to_csv('CAS_result.csv')

if __name__ == '__main__':
    date_to_CAS()
    #name_to_cas()
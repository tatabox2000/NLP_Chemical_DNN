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

def calc_tanimoto():
    df = pd.read_csv('connect_result.csv')
    result_df = pd.DataFrame(index=df['CAS'])
    #fin1 = df['cactvs_fingerprint']
    fin1 =df['isomeric_smiles'].fillna('')

    for i,fin_temp1 in enumerate(fin1):
        print(fin_temp1)
        col=[]
        if fin_temp1 =='':
            pass
        else:
            fin_temp1 =Chem.MolFromSmiles(fin_temp1)
            fin_temp1 = AllChem.GetMACCSKeysFingerprint(fin_temp1)
            for j,fin_temp2 in enumerate(fin1):
                if fin_temp2 =='':
                    result = 'None'
                    col.append(result)
                else:
                    try:
                        fin_temp2 = Chem.MolFromSmiles(fin_temp2)
                        fin_temp2= AllChem.GetMACCSKeysFingerprint(fin_temp2)
                        result = DataStructs.FingerprintSimilarity(fin_temp1,fin_temp2)
                        #print(result)
                        col.append(result)
                    except:
                        result = 'None'
                        col.append(result)
        try:
            result_col_df = pd.DataFrame({df['CAS'][i]:col},index=df['CAS'])
            result_df[df['CAS'][i]] = result_col_df
        except:
            result_col_df = pd.DataFrame({df['CAS'][i]:''},index=df['CAS'])
            result_df[df['CAS'][i]] = result_col_df
        print(result_df.head())
    result_df.to_csv('MACCSKeys_tanimoto.csv')
        #result_df = result_df.append(result_col_df)
        #, columns = df['CAS'][i]
        #print('calc',result_col_df.head(3))
        #print('connect',result_df.head(3))


    # smiles_list = []
    # m = Chem.MolFromSmiles('CCC(CC)O[C@@H]1C=C(C[C@@H]([C@H]1NC(=O)C)[NH3+])C(=O)OCC')
    # m2 = Chem.MolFromSmiles('CCC(CC)O[C@@H]1C=C(C[C@@H]([C@H]1NC(=O)C)[NH3+])C(=O)OCC')
    #
    #
    # #m2 = Chem.MolFromSmiles('c1nccc2n1ccc2')
    # mgfp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024)
    # mgfp2 = AllChem.GetMorganFingerprintAsBitVect(m2, 2, nBits=1024)
    # print(mgfp.GetNumBits())
    # result = DataStructs.FingerprintSimilarity(mgfp,mgfp2)
    #
    # print(result)
    # smi ="CN1CCN(CC2=CC=C(C=C2)C(=O)NC2=CC(NC3=NC=CC(=N3)C3=CN=CC=C3)=C(C)C=C2)CC1"
    # mol = Chem.MolFromSmiles(smi)
    # rdDepictor.Compute2DCoords(mol)
    # mol

    # Chem.Kekulize(mol)
    # drawer = rdMolDraw2D.MolDraw2DSVG(400,200)
    # drawer.DrawMolecule(mol)
    # drawer.FinishDrawing()
    # svg = drawer.GetDrawingText()
    # SVG(svg.replace('svg:',''))
    # Chem.SanitizeMol(mol)

    #highlight=mol.GetSubstructMatch(Chem.MolFromSmarts('c1ccccc1C(=O)N'))
    #highlight=mol.GetSubstructMatch(Chem.MolFromSmarts('ccc'))
    # highlight=mol.GetSubstructMatches(Chem.MolFromSmarts('ccc'))
    #
    # print(highlight)
    # Chem.Kekulize(mol)
    # drawer = rdMolDraw2D.MolDraw2DSVG(400,200)
    # opts = drawer.drawOptions()
    #
    # for i in range(mol.GetNumAtoms()):
    #     opts.atomLabels[i] = mol.GetAtomWithIdx(i).GetSymbol()+str(i)
    #
    # for highlight in highlight:
    #     drawer.DrawMolecule(mol,highlightAtoms=highlight)
    # drawer.FinishDrawing()
    # svg = drawer.GetDrawingText()
    # SVG(svg.replace('svg:',''))
    #
    # fw = open("out.svg","w")
    # fw.write(svg)
    # fw.close()
if __name__ == '__main__':
    calc_tanimoto()
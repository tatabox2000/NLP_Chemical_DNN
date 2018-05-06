import  numpy as np
import pandas as pd
import cirpy
import time
from cirpy import Molecule
import pubchempy as pcp

def cas_to_struc():
    df = pd.read_csv('.\\Data\\toxic_DB2.csv')
    for i , cas in enumerate(df['CAS'].unique()):
        print(i,cas)
    structure_df = pd.DataFrame()
    for i,cas_number in enumerate(df['CAS'].unique()):
        results = {}
        results['smiles'] = cirpy.resolve(cas_number,'smiles')
        iupac_name = cirpy.resolve(cas_number,'iupac_name')
        results['cas_number']=cas_number
        time.sleep(10)

        if isinstance(iupac_name, list)== True:
            iupac_name =iupac_name[0]
        else:
            pass
        results['iupac_name']=iupac_name
        if iupac_name ==None:
            print(iupac_name,'is None')
        else:
            print(iupac_name,'is True')
            pass
            # res3 = cirpy.resolve(iupac_name,'smiles', ['name_by_opsin'])
            # if res3 == None:
            #     print(iupac_name,'no Structure')
            #     # for compound in pcp.get_compounds(iupac_name,'name'):
            #     #     print(compound.molecular_formula)
            # else:
            #     pass
                # mol = Molecule(res3)
                # results['mw'] = mol.mw
                # results['formula'] = mol.formula
                # results['image_url'] = mol.image_url  # The url of a GIF image
                # #results['twirl_url'] = mol.twirl_url  # The url of a TwirlyMol 3D viewer
                # results['stdinchi']=mol.stdinchi
                # results['stdinchikey']= mol.stdinchikey
                # results['ficts'] = mol.ficts
                # results['ficus']= mol.ficus
                # #results['uuuuu'] =  mol.uuuuu
                # results['hashisy']=mol.hashisy
                # results['sdf'] = mol.sdf
                # results['h_bond_donor_count'] = mol.h_bond_donor_count
                # results['h_bond_acceptor_count'] =mol.h_bond_acceptor_count
                # results['h_bond_center_count']=mol.h_bond_center_count
                # results['rule_of_5_violation_count'] =mol.rule_of_5_violation_count
                # results['rotor_count']=mol.rotor_count
                # results['effective_rotor_count']=mol.effective_rotor_count
                # results['ring_count']= mol.ring_count
                # results['ringsys_count'] = mol.ringsys_count


        if structure_df.empty == True:
            structure_df = pd.DataFrame([results.values()],columns=results.keys())
        else:
            results_df = pd.DataFrame([results.values()],columns=results.keys())
            structure_df = structure_df.append(results_df,ignore_index=True)
        print(structure_df.tail(1))
        # if i == 50:
        #     break


    structure_df.to_csv('structure_test.csv')
if __name__ == '__main__':
    cas_to_struc()
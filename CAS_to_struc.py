import  numpy as np
import pandas as pd
import cirpy
from cirpy import Molecule
import pubchempy as pcp

def cas_to_struc():
    df = pd.read_csv('toxic_DB2.csv')

    structure_df = pd.DataFrame()
    for i,cas_number in enumerate(df['CAS'].unique()):
        results = {}
        results['smiles'] = cirpy.resolve(cas_number,'smiles')
        iupac_name = cirpy.resolve(cas_number,'iupac_name')

        results['cas_number']=cas_number

        if isinstance(iupac_name, list)== True:
            iupac_name =iupac_name[0]
        else:
            pass
        results['iupac_name']=iupac_name
        if iupac_name ==None:
            print(iupac_name,'is None')
        else:
            print(iupac_name,'is True')
            res3 = cirpy.resolve(iupac_name,'smiles', ['name_by_opsin'])
            if res3 == None:
                print(iupac_name,'no Structure')
            else:
                mol = Molecule(res3)

                results['mw'] = mol.mw
                results['formula'] = mol.formula

                # stdinchi=mol.stdinchi
                # stdinchikey= mol.stdinchikey
                # ficts = mol.ficts
                # ficus = mol.ficus
                # uuuuu =  mol.uuuuu
                # hashisy=mol.hashisy
                # sdf = mol.sdf
                #
                # image_url = mol.image_url  # The url of a GIF image
                # twirl_url = mol.twirl_url  # The url of a TwirlyMol 3D viewer
                #
                # h_bond_donor_count = mol.h_bond_donor_count
                # h_bond_acceptor_count =mol.h_bond_acceptor_count
                # h_bond_center_count=mol.h_bond_center_count
                # rule_of_5_violation_count =mol.rule_of_5_violation_count
                # rotor_count=mol.rotor_count
                # effective_rotor_count=mol.effective_rotor_count
                # ring_count= mol.ring_count
                # ringsys_count = mol.ringsys_count


        if structure_df.empty == True:
            structure_df = pd.DataFrame([results.values()],columns=results.keys())
        else:
            results_df = pd.DataFrame([results.values()],columns=results.keys())
            structure_df = structure_df.append(results_df,ignore_index=True)
        print(structure_df.tail(5))
        # for compound in pcp.get_compounds(res2,'name'):
        #     print(compound.molecular_formula)
    structure_df.to_csv('structure.csv')
if __name__ == '__main__':
    cas_to_struc()
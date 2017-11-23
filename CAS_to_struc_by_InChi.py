import  numpy as np
import pandas as pd
import cirpy
import time
from cirpy import Molecule
import pubchempy as pcp

property_list2 = ['cid', 'atom_stereo_count', 'atoms', 'bond_stereo_count', 'bonds', 'cactvs_fingerprint',
                         'canonical_smiles', 'charge', 'complexity', 'conformer_id_3d', 'conformer_rmsd_3d',
                         'coordinate_type', 'covalent_unit_count', 'defined_atom_stereo_count',
                         'defined_bond_stereo_count', 'effective_rotor_count_3d', 'elements', 'exact_mass',
                         'feature_selfoverlap_3d', 'fingerprint', 'h_bond_acceptor_count', 'h_bond_donor_count',
                         'heavy_atom_count', 'inchi', 'inchikey', 'isomeric_smiles', 'isotope_atom_count', 'iupac_name',
                         'mmff94_energy_3d', 'mmff94_partial_charges_3d', 'molecular_formula', 'molecular_weight',
                         'monoisotopic_mass', 'multipoles_3d', 'pharmacophore_features_3d', 'record',
                         'rotatable_bond_count', 'shape_fingerprint_3d', 'shape_selfoverlap_3d', 'tpsa',
                         'undefined_atom_stereo_count', 'undefined_bond_stereo_count', 'volume_3d', 'xlogp'
                         ]
def cas_to_struc():
    #df = pd.read_csv('.\\Data\\toxic_DB_debug.csv')
    df = pd.read_csv('.\\Data\\toxic_DB2.csv')

    # for i , cas in enumerate(df['CAS'].unique()):
    #     print(i,cas)
    structure_df = pd.DataFrame()
    for i,cas_number in enumerate(df['CAS'].unique()):

        InChI = cirpy.resolve(cas_number,'InChI')

        print(cas_number)
        #time.sleep(10)

        if isinstance(InChI, list)== True:
            iupac_name =InChI[0]
        else:
            pass
        #iupac_name = iupac_name.replace('InChI=1/','')

        if InChI ==None:
            print(InChI,'is None')
            results_temp_df = pd.DataFrame(columns=property_list2)
            num = 10000000000 + i
            data = pd.DataFrame({'cid': [num], 'CAS': [cas_number]})
            results_temp_df = results_temp_df.append(data)
            results_temp_df.set_index('cid', inplace=True)
            print(results_temp_df)

        else:
            print(InChI,'is True')
            try:
                results_temp_df = pcp.get_compounds(InChI, 'inchi', as_dataframe=True)

            except:
                print('Data is None')
                iupac_name = cirpy.resolve(cas_number, 'iupac_name')

                try:
                    results_temp_df = pcp.get_compounds( iupac_name, 'iupac_name', as_dataframe=True)
                except:
                    print('Data and IUPAC name are None')
                    results_temp_df = pd.DataFrame(columns=property_list2)
                    num = 10000000000 + i
                    data = pd.DataFrame({'cid': [num], 'CAS': [cas_number],'InChI':InChI, 'iupac_name':iupac_name})
                    results_temp_df = results_temp_df.append(data)
                    results_temp_df.set_index('cid', inplace=True)
                    print(results_temp_df)

            if results_temp_df.empty == True:
                #results_temp_df=pd.DataFrame(columns=property_list2)
                num = 10000000000 +i
                data = pd.DataFrame({'cid': [num], 'CAS': [cas_number]})
                results_temp_df = results_temp_df.append(data)
                results_temp_df.set_index('cid',inplace=True)
                print(results_temp_df)

            else:
                results_temp_df['CAS']=cas_number

        if structure_df.empty == True:
            structure_df = results_temp_df
        else:
            structure_df = structure_df.append(results_temp_df)

    structure_df.to_csv('structure_result.csv')

def get_pic_from_cid():
    import os
    df = pd.read_csv('structure_result.csv')
    i = 0
    os.chdir('.//pic_cas')
    for cid,cas in zip(df['cid'],df['CAS']):
        file_name = cas + '.png'
        print(i)
        i += 1
        cid = cid.astype(str)
        print(file_name,cid,cas)
        try:
            pcp.download('PNG', file_name, cid, 'cid')
            print('the picture is exist')
        except:
            print('pic is None')

if __name__ == '__main__':
    #cas_to_struc()
<<<<<<< HEAD
    #get_pic_from_cid()
    print(2662/3221)
=======
    get_pic_from_cid()
>>>>>>> 2a9a9fa43f7008f0da58b4e33730eec949bdf739

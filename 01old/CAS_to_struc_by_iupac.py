import  numpy as np
import pandas as pd
import cirpy
import time
from cirpy import Molecule
import pubchempy as pcp

property_list = ['MolecularFormula','MolecularWeight','CanonicalSMILES','IsomericSMILES','InChI','InChIKey',
                        'IUPACName','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge',
                        'HBondDonorCount','HBondAcceptorCount','RotatableBondCount','HeavyAtomCount',
                        'IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount',
                        'BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount',
                        'Volume3D','XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D',
                        'FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D',
                        'FeatureRingCount3D','FeatureHydrophobeCount3D','ConformerModelRMSD3D',
                        'EffectiveRotorCount3D','ConformerCount3D'
                        ]
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
    df = pd.read_csv('.\\Data\\toxic_DB2.csv')
    # for i , cas in enumerate(df['CAS'].unique()):
    #     print(i,cas)
    structure_df = pd.DataFrame()
    for i,cas_number in enumerate(df['CAS'].unique()):
        results = {}
        #results['smiles'] = cirpy.resolve(cas_number,'smiles')
        #iupac_name = cirpy.resolve(cas_number,'iupac_name')
        iupac_name = cirpy.resolve(cas_number,'InChI')

        results['cas_number']=cas_number
        #time.sleep(10)

        if isinstance(iupac_name, list)== True:
            iupac_name =iupac_name[0]
        else:
            pass
        #iupac_name = iupac_name.replace('InChI=1/','')
        results['iupac_name']=iupac_name

        if iupac_name ==None:
            print(iupac_name,'is None')
            results_temp_df = pd.DataFrame(columns=property_list2)
            num = 10000000000 + i
            data = pd.DataFrame({'cid': [num], 'CAS': [cas_number]})
            results_temp_df = results_temp_df.append(data)
            # results_temp_df['cid']= 10000000000 +i
            results_temp_df.set_index('cid', inplace=True)
            # results_temp_df['CAS']=cas_number
            print(results_temp_df)


        else:
            print(iupac_name,'is True')
            #results_temp_df = pcp.get_compounds(iupac_name, 'name', as_dataframe=True)
            results_temp_df = pcp.get_compounds(iupac_name, 'inchi', as_dataframe=True)
            if results_temp_df.empty == True:
                #results_temp_df=pd.DataFrame(columns=property_list2)
                num = 10000000000 +i
                data = pd.DataFrame({'cid': [num], 'CAS': [cas_number]})
                results_temp_df = results_temp_df.append(data)
                #results_temp_df['cid']= 10000000000 +i
                results_temp_df.set_index('cid',inplace=True)
                #results_temp_df['CAS']=cas_number
                print(results_temp_df)

            else:
                results_temp_df['CAS']=cas_number

        if structure_df.empty == True:
            structure_df = results_temp_df
        else:
            structure_df = structure_df.append(results_temp_df)

        # if i == 80:
        #         structure_df.to_csv('cid.csv')
        #         break

            ##properties select ver
            #for property in property_list:
                # p = pcp.get_properties(property, iupac_name, 'name')
                # results[property] = p[0][property]
                # print(results.values(),results.keys())

                # for compound in pcp.get_compounds(iupac_name,'name'):
            #     print(compound.molecular_formula)
        # if structure_df.empty == True:
        #     structure_df = pd.DataFrame([results.values()],columns=results.keys())
        # else:
        #     results_df = pd.DataFrame([results.values()],columns=results.keys())
        #     structure_df = structure_df.append(results_df,ignore_index=True)
        # print(structure_df.tail(1))
        # if i == 50:
        #     break

    structure_df.to_csv('structure_result.csv')
if __name__ == '__main__':
    cas_to_struc()
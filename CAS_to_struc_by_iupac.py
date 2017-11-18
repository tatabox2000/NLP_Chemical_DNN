import  numpy as np
import pandas as pd
import cirpy
import time
from cirpy import Molecule
import pubchempy as pcp

property_list = ['MolecularFormula','MolecularWeight','CanonicalSMILES','IsomericSMILES','InChI','InChIKey','IUPACName','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge','HBondDonorCount','HBondAcceptorCount','RotatableBondCount','HeavyAtomCount','IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount','BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount','Volume3D','XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D','FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D','FeatureRingCount3D','FeatureHydrophobeCount3D','ConformerModelRMSD3D','EffectiveRotorCount3D','ConformerCount3D']

def cas_to_struc():
    df = pd.read_csv('.\\Data\\toxic_DB2.csv')
    # for i , cas in enumerate(df['CAS'].unique()):
    #     print(i,cas)
    structure_df = pd.DataFrame()
    for i,cas_number in enumerate(df['CAS'].unique()):
        results = {}
        #results['smiles'] = cirpy.resolve(cas_number,'smiles')
        iupac_name = cirpy.resolve(cas_number,'iupac_name')
        iupac_name = cirpy.resolve(cas_number,'InChI')

        results['cas_number']=cas_number
        time.sleep(10)

        if isinstance(iupac_name, list)== True:
            iupac_name =iupac_name[0]
        else:
            pass
        #iupac_name = iupac_name.replace('InChI=1/','')
        results['iupac_name']=iupac_name

        if iupac_name ==None:
            print(iupac_name,'is None')
        else:
            print(iupac_name,'is True')
            #results_temp_df = pcp.get_compounds(iupac_name, 'name', as_dataframe=True)
            results_temp_df = pcp.get_compounds(iupac_name, 'inchi', as_dataframe=True)

            results_temp_df['CAS']=cas_number

            if structure_df.empty == True:
                structure_df = results_temp_df
            else:
                structure_df = structure_df.append(results_temp_df)

        if i == 10:
                structure_df.to_csv('cid.csv')
                break

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

    structure_df.to_csv('structure_test.csv')
if __name__ == '__main__':
    cas_to_struc()
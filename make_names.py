

def make_name(name_list):
    name_list = name_list.replace(',','\',\'')
    name_list = name_list.replace(' ','')

    print(name_list)


if __name__ == '__main__':
    name_list = 'cid,atom_stereo_count,atoms,bond_stereo_count,bonds,cactvs_fingerprint,canonical_smiles,charge,complexity,conformer_id_3d,conformer_rmsd_3d,coordinate_type,covalent_unit_count,defined_atom_stereo_count,defined_bond_stereo_count,effective_rotor_count_3d,elements,exact_mass,feature_selfoverlap_3d,fingerprint,h_bond_acceptor_count,h_bond_donor_count,heavy_atom_count,inchi,inchikey,isomeric_smiles,isotope_atom_count,iupac_name,mmff94_energy_3d,mmff94_partial_charges_3d,molecular_formula,molecular_weight,monoisotopic_mass,multipoles_3d,pharmacophore_features_3d,record,rotatable_bond_count,shape_fingerprint_3d,shape_selfoverlap_3d,tpsa,undefined_atom_stereo_count,undefined_bond_stereo_count,volume_3d,xlogp'
    #name_list = 'MolecularFormula, MolecularWeight, CanonicalSMILES, IsomericSMILES, InChI, InChIKey, IUPACName, XLogP, ExactMass, MonoisotopicMass, TPSA, Complexity, Charge, HBondDonorCount, HBondAcceptorCount, RotatableBondCount, HeavyAtomCount, IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, UndefinedAtomStereoCount, BondStereoCount, DefinedBondStereoCount, UndefinedBondStereoCount, CovalentUnitCount, Volume3D, XStericQuadrupole3D, YStericQuadrupole3D, ZStericQuadrupole3D, FeatureCount3D, FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D, FeatureHydrophobeCount3D, ConformerModelRMSD3D, EffectiveRotorCount3D, ConformerCount3D'
    make_name(name_list)
    #['MolecularFormula','MolecularWeig', 'ht','CanonicalSMILES','IsomericSMILES','InChI','InChIKey','IUPACName','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge','HBondDonorCount','HBondAcceptorCount','RotatableBondCount','HeavyAtomCount','IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount','BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount','Volume3D','XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D','FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D','FeatureRingCount3D','FeatureHydrophobeCount3D','ConformerModelRMSD3D','EffectiveRotorCount3D','ConformerCount3D']

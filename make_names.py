

def make_name(name_list):
    name_list = name_list.replace(',','\',\'')
    name_list = name_list.replace(' ','')

    print(name_list)


if __name__ == '__main__':
     name_list = 'MolecularFormula, MolecularWeight, CanonicalSMILES, IsomericSMILES, InChI, InChIKey, IUPACName, XLogP, ExactMass, MonoisotopicMass, TPSA, Complexity, Charge, HBondDonorCount, HBondAcceptorCount, RotatableBondCount, HeavyAtomCount, IsotopeAtomCount, AtomStereoCount, DefinedAtomStereoCount, UndefinedAtomStereoCount, BondStereoCount, DefinedBondStereoCount, UndefinedBondStereoCount, CovalentUnitCount, Volume3D, XStericQuadrupole3D, YStericQuadrupole3D, ZStericQuadrupole3D, FeatureCount3D, FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D, FeatureHydrophobeCount3D, ConformerModelRMSD3D, EffectiveRotorCount3D, ConformerCount3D'
     make_name(name_list)
     ['MolecularFormula','MolecularWeig', 'ht','CanonicalSMILES','IsomericSMILES','InChI','InChIKey','IUPACName','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge','HBondDonorCount','HBondAcceptorCount','RotatableBondCount','HeavyAtomCount','IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount','BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount','Volume3D','XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D','FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D','FeatureRingCount3D','FeatureHydrophobeCount3D','ConformerModelRMSD3D','EffectiveRotorCount3D','ConformerCount3D']

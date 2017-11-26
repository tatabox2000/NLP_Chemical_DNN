import pylab as plt
from rdkit.Chem import AllChem as Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem.Draw import SimilarityMaps

smiles1 = 'N[C@H](CC(=O)O)C(=O)O'  # ZINC000000895218 (D-Aspartate)
smiles2 = 'N[C@@H](CO)C(=O)O'  # ZINC000000895034 (L-Ser)

mol1 = Chem.MolFromSmiles(smiles1)
mol2 = Chem.MolFromSmiles(smiles2)

result = SimilarityMaps.GetSimilarityMapForFingerprint(mol2, mol1, SimilarityMaps.GetMorganFingerprint)
plt.show()
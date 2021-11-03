# conda install -c rdkit rdkit
import rdkit
rdkit.__version__


# mol -> smiles
from rdkit import Chem
from rdkit.Chem import Draw
mol_file = 'data/AAQ.mol'
mol = Chem.MolFromMolFile(mol_file)
smiles = Chem.MolToSmiles(mol)
#画分子图
# Draw.MolToFile(mol,'img/AAQ.png')
Draw.MolToImage(mol, size=(100, 100),fitImage=True)
#print(img)
#print(f'{mol}\n{smiles}')


# smiles -> mol
smile = 'COC1=C(C=C2C(=C1)CCN=C2C3=CC(=C(C=C3)Cl)Cl)Cl'
mol = Chem.MolFromSmiles(smile)
print(f'{mol}')
# 保存mol文件
Chem.MolToMolFile(mol,'data/CHEMBL1087421.mol')
#打印mol格式内容
print(Chem.MolToMolBlock(mol)) 


# sdf -> smiles
from rdkit.Chem import AllChem
sdf_file = 'data/Structure2D_CID_44138048.sdf'
mol = Chem.MolFromMolFile(sdf_file)
smiles = Chem.MolToSmiles(mol)
print(f'{mol}\n{smiles}')




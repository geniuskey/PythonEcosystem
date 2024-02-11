from rdkit import Chem
from rdkit.Chem import Descriptors, Draw

# 분자 생성 (아스피린)
aspirin = Chem.MolFromSmiles('O=C(C)Oc1ccccc1C(=O)O')

# 분자의 분자량 계산
mol_weight = Descriptors.MolWt(aspirin)
print(f'아스피린의 분자량: {mol_weight}')

# 분자 구조 시각화
Draw.MolToImage(aspirin)

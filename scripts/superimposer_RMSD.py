import Bio
from Bio.PDB import *

start_id = 3
end_id   = 45
atoms_to_be_aligned = range(start_id, end_id + 1)

pdb1 = PDBList()
parser = MMCIFParser(QUIET = True)
pdb1.retrieve_pdb_file('3war')
pdb1.retrieve_pdb_file('3bqc')
ref_structure=parser.get_structure('3WAR','3war.cif')
sample_structure=parser.get_structure('3BQC','3bqc.cif')

ref_model    = ref_structure[0]  #select the first model
sample_model = sample_structure[0]

ref_atoms = []
sample_atoms = []


for ref_chain in ref_model:
  for ref_res in ref_chain:
    if ref_res.get_id()[1] in atoms_to_be_aligned:
      ref_atoms.append(ref_res['CA'])
      
      
for sample_chain in sample_model:
  for sample_res in sample_chain:
    if sample_res.get_id()[1] in atoms_to_be_aligned:
      sample_atoms.append(sample_res['CA'])

#superimposer
super_imposer =Superimposer()
super_imposer.set_atoms(ref_atoms, sample_atoms)
super_imposer.apply(sample_model.get_atoms())

#RMSD
print (super_imposer.rms)

io =PDBIO()
io.set_structure(sample_structure) 
io.save("aligned.pdb")
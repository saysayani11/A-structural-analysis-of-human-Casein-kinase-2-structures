from Bio.PDB.MMCIFParser import MMCIFParser
parser = MMCIFParser()
structure = parser.get_structure("4nc6", "4nc6.cif")
for model in structure:
    for chain in model:
         for residue in chain:
            for atom in residue:
                print(atom, atom.get_bfactor(),atom.get_occupancy())
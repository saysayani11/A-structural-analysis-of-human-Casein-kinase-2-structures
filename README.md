# COMPUTATIONAL INVESTIGATION OF PROTEIN STRUCTURES (HUMAN CK2A)

## TASK:

The task aims at analyzing various structures of human casein kinase 2 alpha subunit from the PDB, solved at different resolutions, differing among each other with respect to bound ligands/molecules. Analysis includes extraction of common regions from all the structures and studying their RMSD and B-Factor plots. 

## SUMMARY:

3D representative structures of proteins give insights into mechanisms of disease and allow the design of diagnostic agents. A computational understanding of structures along with experimental data is advantageous. Several methods popularly used to determine the structure of a protein are X-Ray Crystallography, NMR Spectroscopy and Cryo-electron microscopy. The Protein Data Bank (PDB) is a repository of such solved structures of biomolecules using these experimental techniques. It allows for searching and exploring deposited structures under a unique PDB entry. The PDB file holds the following information:

1.	HEADER, TITLE, AUTHOR records
2.	REMARK records
3.	SEQRES records
4.	ATOM records
5.	HETATOM records

Often the most used information in a structure file is the coordinates of each ATOM record that describes the atom’s location in #D space, an associated occupancy and a temperature factor. 

The **Root Mean Square Deviation (RMSD)** is a measure of the average distance between ATOMS, usually the CA-backbones. It can be used as a measure of similarity between structures. To calculate RMSD, we perform a geometric translation followed by a rotation of one structure over the target structure. Given a set of n points, the RMSD between two protein structure backbones were calculated using formula thereby obtaining a good, minimized RMSD. A stacked line-plot of the RMSD all protein structures showed some regions of variability across all the structures. Using visualization software UCSF Chimera, it was observed that most of these variabilities come from loop regions.

The **B-factor** describes the displacement of the atomic positions from an average value (mean-square displacement). Residue-wise B-factor plots were generated for the 
20 structures using Biopython. It was seen that regions with low local residue B-factors corresponded to the stable regions in the protein structure, like helices and sheets, whereas regions with high local B-factors corresponded to flexible regions in the protein structure, like loops. Comparing the B-factor plots of the 20 structures, it was found that at good resolutions, the per residue B factors were low, ie., uncertainty in atomic positions was low. This is reflective of the fact that at poor resolutions, ( low empirical electron density) higher temperature factors and hence disorder is observed.

## STEPS:

PDB IDs
1. 3bqc: High pH-value crystal structure of emodin in complex with the catalytic subunit of protein kinase CK2 (1.5A)
2. 3h30: Crystal structure of the catalytic subunit of human protein kinase CK2 with 5,6-dichloro-1-beta-D-ribofuranosylbenzimidazole (1.56Å)
3. 3mb7: Human CK2 catalytic domain in complex with a difurane derivative inhibitor (AMR) (1.65 Å)
4. 3nsz: Human CK2 catalytic domain in complex with AMPPN (1.30 Å)
5. 3pe1: Crystal structure of human protein kinase CK2 alpha subunit in complex with the inhibitor CX-4945 (1.6 Å)
6. 3war: Crystal structure of human CK2a (1.04 Å)
7. 4kwp: Crystal Structure of Human CK2-alpha in complex with a benzimidazole inhibitor (K164) at 1.25 A resolution (1.25 Å)
8. 5csv: Crystal Structure of CK2alpha with Compound 6 bound (1.375 Å)
9. 5cu4: Crystal Structure of CK2alpha with Compound 10 bound (1.56 Å)
10. 5cu6: Crystal Structure of CK2alpha (1.36 Å)
11. 2pvr: Crystal structure of the catalytic subunit of protein kinase CK2 (C-terminal deletion mutant 1-335) in complex with two sulfate ions
12. 5clp: Crystal Structure of CK2alpha with 3,4-dichlorophenethylamine bound
13. 5csp: Crystal Structure of CK2alpha with Compound 5 bound
14. 5cvg: Crystal Structure of CK2alpha with a novel closed conformation of the aD loop
15. 3r0t: Crystal structure of human protein kinase CK2 alpha subunit in complex with the inhibitor CX-5279
16. 3q9w: Crystal structure of human CK2 alpha in complex with emodin at pH 8.5
17. 3q04: Crystal structure of the apo-form of human CK2 alpha at pH 8.5
18. 5cs6: Crystal Structure of CK2alpha with Compound 3 bound
19. 3owk: Human CK2 catalytic domain in complex with a benzopyridoindole derivative inhibitor
20. 4rll: Crystal structure of human CK2alpha in complex with the ATP-competitive inhibitor 4-[(E)-(fluoren-9-ylidenehydrazinylidene)-methyl] benzoate

MSA 
Files: 
sequences_pdb20.pir
sequences_pdb20.fasta

Input file for alignment using Bio. Align; MSA generated

Set Reference: 3war - Crystal structure of human CK2a (1.04 Å)
Set Sample: x – any of the other 19 structures

Define Ranges, Extract CA co-ordinates from Reference and Sample 

30-300 bps
Biopython script


## DATA AVAILABILITY:

The structural information of 20 human CK2A in various bound/free forms have been extracted from their respective PDB files.
The dataset in placed as a folder located in the main repository.

## CODE AVAILABILITY:

The scripts folder placed at the main repository contains all scripts. 

## QUERIES:

Please drop an email at: say.Sayani11@gmail.com


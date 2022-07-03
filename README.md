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

1. Download PDB files for 20 human CK2A structures.
2. Perform MSA and extract the common 30 - 300 bps from all of the structures for further analysis.
3. Extract CA coordinates
4. **RMSD Analyis: ** 
5. **B Factor analyis: ** 
6. 

For detailed information please download steps.docx file from the main repository


## DATA AVAILABILITY:

The structural information of 20 human CK2A in various bound/free forms have been extracted from their respective PDB files.
The dataset in placed as a folder located in the main repository.

## CODE AVAILABILITY:

The scripts folder placed at the main repository contains all scripts. 

## QUERIES:

Please drop an email at: say.Sayani11@gmail.com


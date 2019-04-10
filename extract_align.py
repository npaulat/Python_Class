#Import python packages
import os
from Bio import SeqIO
import argparse
import pandas as pd
import numpy as np

###################################################################
###################################################################
##                                                               ##
##  extract.align.pl - a program to extract TEs from a genome    ##
##                                                               ##
##  Required values:                                             ##
##    --genome    input genome file (in fasta format)            ##
##    --blast     input blast file (tab format [6])              ##
##    --consTEs   file of consensus elements                     ##
##    --seqBuffer additional 5'/3' bases in extracted sequence   ##
##    --seqNum    number of sequences to extract                 ##
##                                                               ##
##  Optional values:                                             ##
##    --align     aligns the sequences with MUSCLE               ##
##                                                               ##
###################################################################
###################################################################

#Set arguments for command line

parser=argparse.ArgumentParser()
parser.add_argument('-gen', '--genome', help='input genome file (in fasta format)', required=True)
parser.add_argument('-blst', '--blast', type=str, help='input blast file (tab format [6])', required=True)
parser.add_argument('-cons', '--consTEs', type=str, help='file of consensus elements', required=True)
parser.add_argument('-buf', '--seqBuffer', type=int, help='additional 5 prime and 3 prime bases in extracted sequence', default=500)
parser.add_argument('-num', '--seqNum', type=int, help='number of sequences to extract', default=40)
args=vars(parser.parse_args())

#Make shorthand arguments:
GENOME=args["genome"]
BLAST=args["blast"]
CONSTES=args["consTEs"]
BUFFER=args["seqBuffer"]
NUMBER=args["seqNum"]


####################################################
##  STEP 1 - Create the processed_blast.txt file  ##
####################################################

#Create the processed_blast.txt file for writing
BLAST_OUT = open("processed_blast.txt", "w")

# Read the blast output into pandas, only include info we care about:
# TE_Name, Contig, Start, Stop, E-Value, Bit-Score
BLAST_INPUT = pd.read_csv(BLAST, sep='\t', lineterminator='\n', header=None, usecols=[0,1,8,9,10,11])

# Create a list of all the queried TEs for this round
LIST_TES_QUERIED=[]
for record in SeqIO.parse(CONSTES,'fasta'):
        LIST_TES_QUERIED.append(str(record.id))


# Use a for-loop to create the processed_blast.txt file.

# For each queried TE
for i in LIST_TES_QUERIED:

        # Find all the hits for that TE in the blast input file
        TE_HIT_DATA = BLAST_INPUT.loc[BLAST_INPUT[0] == i ]

        # Sort the blast hits for this TE by evalue (small to big)
        SORTED_EVALUE = TE_HIT_DATA.sort_values(by=[10])

        # Sort again by the bit score (big to small).
        SORTED_BITSCORE = SORTED_EVALUE.sort_values(by=[11], ascending=False)

        #Remove the E-Value and Bit-Score columns from the dataframe
        DROPPED_COLUMNS = SORTED_BITSCORE.drop(columns=[10,11])

        #Create a new column with the length between start & stop
        DROPPED_COLUMNS['12'] = (DROPPED_COLUMNS[9] - DROPPED_COLUMNS[8])

        #If the length is >0, then put 1... if <0, then put -1
#       DROPPED_COLUMNS['13'] = DROPPED_COLUMNS['12'].apply(lambda x: '1' if x > 0 else '-1')
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['12'] < 0, '13'] = '-1'
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['12'] > 0, '13'] = '1'
#       DROPPED_COLUMNS = DROPPED_COLUMNS.astype({'13': int})
        DROPPED_COLUMNS['13'] = pd.to_numeric(DROPPED_COLUMNS['13'])

        #Creating a new "start" column... this is clunky, but it works
#       DROPPED_COLUMNS['14'] = DROPPED_COLUMNS['13'].apply(lambda x: [8] if x == 1 else '0')
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['13'] == 1, '14'] = DROPPED_COLUMNS[8]
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['13'] < 0, '14'] = '0'
#       DROPPED_COLUMNS = DROPPED_COLUMNS.astype(int)
        DROPPED_COLUMNS['14'] = pd.to_numeric(DROPPED_COLUMNS['14'])
#       DROPPED_COLUMNS['15'] = DROPPED_COLUMNS['13'].apply(lambda x: [9] if x == -1 else '0')
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['13'] == -1, '15'] = DROPPED_COLUMNS[9]
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['13'] > 0, '15'] = '0'
#       DROPPED_COLUMNS = DROPPED_COLUMNS.astype({'15': int})
        DROPPED_COLUMNS['15'] = pd.to_numeric(DROPPED_COLUMNS['15'])
        DROPPED_COLUMNS['16'] = (DROPPED_COLUMNS['14'] + DROPPED_COLUMNS['15'])
        DROPPED_COLUMNS['17'] = (DROPPED_COLUMNS['16'] - BUFFER)
#       DROPPED_COLUMNS['18'] = DROPPED_COLUMNS['17'].apply(lambda x: 0 if x < 0 else ['17'])
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['17'] < 0, '18'] = '0'
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS['17'] > 0, '18'] = DROPPED_COLUMNS['17']
#       DROPPED_COLUMNS = DROPPED_COLUMNS.astype({'18': int})
        DROPPED_COLUMNS['18'] = pd.to_numeric(DROPPED_COLUMNS['18'])

        #Creating a new length column... again... mind the clunkiness
        DROPPED_COLUMNS['19'] = DROPPED_COLUMNS['12'].abs()


        DROPPED_COLUMNS['17'] = pd.to_numeric(DROPPED_COLUMNS['17'])
        DROPPED_COLUMNS['19'] = pd.to_numeric(DROPPED_COLUMNS['19'])

        DROPPED_COLUMNS['20'] = (2*BUFFER+DROPPED_COLUMNS['19']+DROPPED_COLUMNS['17']-DROPPED_COLUMNS['18'])

        #Move the forward and reverse information back to the end of the dataframe
        DROPPED_COLUMNS['21'] = DROPPED_COLUMNS['13']

        #Cleaning up the dataframe to get rid of all the excess crap
#       CLEAN_DF = DROPPED_COLUMNS['8','9','12','13','14','15','16','17','19'].drop()
        CLEAN_DF = DROPPED_COLUMNS.drop(columns=['8','9','12','13','14','15','16','17','19'])



        #Finally, write out the processed_blast.txt file
        BLAST_OUT.write(str(CLEAN_DF.head(NUMBER)))



#########################################################################
# STEP 2 - figure out how to flip the sequence if blast hit is backwards
# There's a biopython implementation for this "reverse_compliment()

#for record in SeqIO.parse(????, "fasta"):
#       FLIPPED = record.reverse_compliment(????)


# PSEUDOCODE
#If the processed_blast.txt file contains a -1 at the end of the line, pull sequence out, reverse it, print it to file.
#If the processed_blast.txt file contains a 1 at the end of the line, pull the sequence out, print it to file.

#Import python packages
import re
import os
from Bio import SeqIO
import argparse
import pandas as pd
import numpy as np
import subprocess

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
parser.add_argument('-aln', '--align', type=str, help='aligns the sequnces with MUSCLE', default=False, required=False)
args=vars(parser.parse_args())

#Make shorthand arguments:
MUSCLE=args["align"]
GENOME=args["genome"]
BLAST=args["blast"]
CONSTES=args["consTEs"]
BUFFER=args["seqBuffer"]
NUMBER=args["seqNum"]


####################################################
##  STEP 1 - Create the processed_blast.txt file  ##
####################################################

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
        DROPPED_COLUMNS[12] = (DROPPED_COLUMNS[9] - DROPPED_COLUMNS[8])

        #If the length is >0, then put 1... if <0, then put -1
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[12] < 0, 13] = '-1'
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[12] > 0, 13] = '1'
        DROPPED_COLUMNS[13] = pd.to_numeric(DROPPED_COLUMNS[13])

        #Creating a new "start" column... this is clunky, but it works
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[13] == 1, 14] = DROPPED_COLUMNS[8]
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[13] < 0, 14] = '0'
        DROPPED_COLUMNS[14] = pd.to_numeric(DROPPED_COLUMNS[14])
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[13] == -1, 15] = DROPPED_COLUMNS[9]
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[13] > 0, 15] = '0'
        DROPPED_COLUMNS[15] = pd.to_numeric(DROPPED_COLUMNS[15])
        DROPPED_COLUMNS[16] = (DROPPED_COLUMNS[14] + DROPPED_COLUMNS[15])
        DROPPED_COLUMNS[17] = (DROPPED_COLUMNS[16] - BUFFER)
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[17] < 0, 18] = '0'
        DROPPED_COLUMNS.loc[DROPPED_COLUMNS[17] > 0, 18] = DROPPED_COLUMNS[17]
        DROPPED_COLUMNS[18] = pd.to_numeric(DROPPED_COLUMNS[18], downcast='signed')

        #Creating a new length column.
        DROPPED_COLUMNS[19] = DROPPED_COLUMNS[12].abs()
        DROPPED_COLUMNS[17] = pd.to_numeric(DROPPED_COLUMNS[17])
        DROPPED_COLUMNS[19] = pd.to_numeric(DROPPED_COLUMNS[19])
        DROPPED_COLUMNS[20] = (2*BUFFER+DROPPED_COLUMNS[19]+DROPPED_COLUMNS[17]-DROPPED_COLUMNS[18])
        DROPPED_COLUMNS[20] = pd.to_numeric(DROPPED_COLUMNS[20], downcast='signed')

        #Move the forward and reverse information back to the end of the dataframe
        DROPPED_COLUMNS[21] = DROPPED_COLUMNS[13]

        #Cleaning up the dataframe to get rid of all the excess crap
        CLEAN_DF2 = DROPPED_COLUMNS.drop(columns=[8,9,12,13,14,15,16,17,19])

        #Finally, write the output to an itermediate file which will be deleted later.
        CLEAN_DF2.head(NUMBER).to_csv("processed_blast.txt",sep='\t',mode='a',header=False,index=False)


#########################################################################
#      STEP 2 - Create a new sequence file for every queried TE         #
#########################################################################

for record in SeqIO.parse(CONSTES, 'fasta'):
        FIXED_ID = re.sub('#', '__', record.id)
        FIXED_ID = re.sub('/', '___', FIXED_ID)
        record.id = 'CONSENSUS-' + FIXED_ID
        record.description = ''
        SeqIO.write(record, FIXED_ID + '.fas', 'fasta')


#########################################################################
#   STEP 3 - Populate the new sequence files with extracted blast hits  #
#########################################################################

with open("processed_blast.txt", 'r') as BED:
        for line in BED:
                TE_BED, CONTIG, START, LENGTH, ORIENT = line.split()
                STOP = int(START) + int(LENGTH)
                for seq in SeqIO.parse(GENOME, "fasta"):
                        chrs = {}
                        chrs[seq.id]=seq.seq
                        if CONTIG == seq.id:
                                for TE in LIST_TES_QUERIED:
                                        with open(TE+".fas", 'a') as out:
                                                if TE_BED == TE:
                                                        if ORIENT == 1:
                                                                out.write(str(">" + CONTIG + "-" + str(START) + "-" + str(STOP) + "(" + str(ORIENT) + ")" + '\n'))
                                                                out.write(str(chrs[CONTIG][int(START):int(STOP)] + "\n"))
                                                        else:
                                                                out.write(str(">" + CONTIG + "-" + str(START) + "-" + str(STOP) + "(" + str(ORIENT) + ")" + '\n'))
                                                                sequence = chrs[CONTIG][int(START):int(STOP)]
                                                                out.write(str(sequence.reverse_complement() + "\n"))
out.close()


#########################################################################
#         STEP 4 - Align the TE output files if specified               #
#########################################################################

SOFTWARE = '/lustre/work/daray/software/muscle/'

if MUSCLE == 'True':
        for FILE in LIST_TES_QUERIED:
                ALN_COMMAND = "{}muscle -in {} -out {}".format(SOFTWARE, FILE+".fas", FILE+".muscle.fas")
                subprocess.run(ALN_COMMAND, shell=True)

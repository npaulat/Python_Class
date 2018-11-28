import sys
import os
import argparse
import subprocess

##############################################
#This week's task:
#Use python to:
#1. run blast: blastn -query <TE library> -db <genome> -out <arbitrary name of outfile> -outfmt 6 (is to make it tab delimited)
#2. run extractAlignTEs.pl: extractAlignTEs.pl -genome <genome> -blast <blast output file> -consTEs <TE library> -seqBuffer <# of bps flanking TE> --seqNum <# of closest blast hits> -align

#Starting files are as follows:
#cPer_rn.fa.gz
#extractAlignTEs.pl
#starting_library.fas
##############################################

#Set arguments for command line

parser=argparse.ArgumentParser()
parser.add_argument('-gen', '--genome', help='data input file - FASTA', required=True)
parser.add_argument('-loc', '--location', type=str, help='full location of working directory, i.e. no period', required=True)
parser.add_argument('-lib', '--TElibrary', type=str, help='The TE library to blast your genome with' , required=True)
parser.add_argument('-flank', '--flankingseq', type=int, help='The number of bps flanking the blasted TEs', required=True)
parser.add_argument('-num', '--seqnum', type=int, help='The number of closest blast hits included in extractAlign output', required=True)
args=vars(parser.parse_args())

#Make shorthand arguments:
GEN=args["genome"]
LOC=args["location"]
LIB=args["TElibrary"]
FLANK=args["flankingseq"]
SEQNUM=args["seqnum"]

#Sanity Check
print('The genome file is:', GEN)
print('The location is:', LOC)
print('The library you are using  is:', LIB)
print('Flanking sequence length is:', FLANK)
print('Number of blast hits in ExtractAlign:', SEQNUM)

#Index the genome
subprocess.check_call('samtools faidx {}'.format(GEN),shell=True)

#Create Blast Database
subprocess.check_call('makeblastdb -in {} -dbtype nucl'.format(GEN),shell=True)

#Call blastn
subprocess.check_call('blastn -query {} -db {} -out blast_results -outfmt 6'.format(LIB, GEN), shell=True)

#Run Extract Align
subprocess.check_call('perl {}/extractAlignTEs.pl -genome {} -blast ExAlign_out -consTEs {} -seqBuffer {} -seqNum {} -align'.format(LOC, GEN, LIB, FLANK, SEQNUM), shell=True

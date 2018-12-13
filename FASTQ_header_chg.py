from Bio import SeqIO
import sys
import argparse

################################################################
################################################################
#####                Python Assignment #3                 ######
##### Creating sliding windows and Calculating GC content ######
################################################################

##### Steps to take #####
# 3. Required output to present in two weeks:
# a. a fully formed, submittable script... python <name of script> -<input, output, options>
# b. must take input and output arguments, as well as an argument for the number of digits in the read ID
# c. output in .fastq format

################################################################
################################################################

#Set arguments for command line
parser=argparse.ArgumentParser()
parser.add_argument('-data', '--data', help='data input file - FASTQ', required=True)
parser.add_argument('-loc', '--location', type=str, help='full location of working directory, i.e. no period', required=True)
args=vars(parser.parse_args())

#Make shorthand arguments:
DATA=args["data"]
LOC=args["location"]

#Sanity Check
print('The data file is:', DATA)
print('The location is:', LOC)


#Navigate to home directory
os.chdir(LOC)

#Replace the trailing part of the header with a new system:
with gzip.open(DATA, 'rt') as OLD:
    # 1:N:0:1 > OP:i:1
    OLD.replace("1:N:0:1", "OP:i:1")
    # 2:N:0:1 > OP:i:2
    OLD.replace("2:N:0:1", "OP:i:2")

#Initialize numbering system at one
COUNT = 0

#Create a new dictionary for new sequence IDs
NEW_RECORDS=[]

#open up the .gz fasta file using BioPython
with gzip.open(DATA, "rt") as FASTQ_IN:
    for seq_record in SeqIO.parse(FASTQ_IN, "fastq"):
        #Set the Count
        COUNT += 1
        #Set the contig's naming with 15 leading zeros
        CONTIG = '{:0>15}'.format(COUNT//2+1)
        #Sanity Check
        print(CONTIG)

        #Replace with the new contig name, "header"
        seq_record.description = seq_record.description.replace(seq_record.id, "")
        seq_record.id = CONTIG

        #Append to the NEW_RECORDS list
        NEW_RECORDS.append(seq_record)
    #Finally, write out the full new header.        
    SeqIO.write(NEW_RECORDS, DATA, "fastq")


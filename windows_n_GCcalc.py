import os
from Bio import SeqIO
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
from Bio.SeqUtils import GC
import argparse

################################################################
################################################################
#####                Python Assignment #3                 ######
##### Creating sliding windows and Calculating GC content ######
################################################################

##### Steps to take #####
# 1. Only use scaffolds with a minimum length (Ex: 30,000 bp)
# 2. Create sliding windows of given length (Ex: 10,000 bp) using "def" function
# 3. Calculate GC content for each window using "def" function
# 4. Plot frequency histogram

##### Arguments #####
# 1. Input file
# 2. Output plot file
# 3. Minimum length of scaffold
# 4. Length of window

################################################################
################################################################

#Set arguments for command line

parser=argparse.ArgumentParser()
parser.add_argument('-data', '--data', help='data input file - FASTA', required=True)
parser.add_argument('-loc', '--location', type=str, help='full location of working directory, i.e. no period', required=True)
parser.add_argument('-out', '--output', type=str, help='name of the histogram output file', required=True)
parser.add_argument('-minlen', '--minlen', type=int, help='minimum length of scaffold... default is 10kb', default=10000)
parser.add_argument('-window', '--window', type=int, help='size of the window... default is 10kb', default=10000)
args=vars(parser.parse_args())

#Make shorthand arguments:
DATA=args["data"]
LOC=args["location"]
OUT=args["output"]
MINLEN=args["minlen"]
WINDOW=args["window"]

#Sanity Check
print('The data file is:', DATA)
print('The location is:', LOC)
print('The output file name is:', OUT)
print('The minimum contig length is:', MINLEN)
print('The window size is:', WINDOW,'kb')

os.chdir(LOC)

################################################################
# Set up a new file with contigs of MINLEN
################################################################

#Create a new file that meets the minimum length criteria.
MINLENLIST = []
for record in SeqIO.parse(DATA, 'fasta'):
        if len(record) >= MINLEN:
                MINLENLIST.append(record)
SeqIO.write(MINLENLIST, "min_length.fas", 'fasta')
MINLEN_FAS=(LOC + '/min_length.fas')

################################################################
# Create a new fasta file with contigs adjusted to window length
################################################################

#Following the stackoverflow threads:
#https://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator
#https://stackoverflow.com/questions/30317400/python-how-to-print-out-sequences-with-length-n-from-sliding-window-in-fasta-fi

def create_windows(chunk, WINDOW):
        count = 0
        for BEGIN in range(0, len(record.seq), WINDOW):
                count += 1
                END = BEGIN + WINDOW
                if END > len(record.seq):
                        break
                yield BEGIN, END, count

with open("windows.fas",'w') as window_fas:
        for record in SeqIO.parse(MINLEN_FAS, 'fasta'):
                chunk=record.seq
                for BEGIN, END, count in create_windows(chunk, WINDOW):
                        window_fas.write(">" + str(record.id) + "_window_" + str(count) + '\n')
                        window_fas.write(str(record.seq[BEGIN:BEGIN+WINDOW]) + '\n')
window_fas.close()
WINDOWS=(LOC + '/windows.fas')

###########################################################################
# Calculate the GC content of each contig in windows.fas and plot histogram
###########################################################################

def gc_calc():
        ALL_GC = []
        with open("gc_content.txt", 'w') as GC_FILE:
                for sequence in SeqIO.parse(WINDOWS, 'fasta'):
                        RECORD_GC = GC(sequence.seq)
                        ALL_GC.append(RECORD_GC)
                        GC_FILE.write(str(sequence.id) + "\t" + str(RECORD_GC) + "\n")

        #Plot Histogram
        plt.hist(x=ALL_GC, bins = "auto")
        plt.xlabel("Average GC content per window")
        plt.ylabel("Frequency of averages among the windows")
        plt.savefig(OUT)

if __name__ =='__main__':gc_calc()

#boxplot.py v1.0
#create a box and whisker plot from input data
#A.B.Osmanski - 18 Sept 2018
#Manual for boxplots using python can be found here:
#https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.boxplot.html

#Import modules
import sys
import os
import argparse
import matplotlib
matplotlib.use('agg')
import pylab as plt
import numpy as np
import pandas as pd

#Set arguments for command line
def get_args():
        parser=argparse.ArgumentParser()
        parser.add_argument('-data', '--data', help='data input file', required=True)
        parser.add_argument('-loc', '--location', type=str, help='full location of working directory, i.e. no period', required=True)
        parser.add_argument('-grid', '--gridlines', type=str, help="'False', to remove gridlines on your boxplot")
        parser.add_argument('-font', '--fontsize', type=str, help="Select a font size for your boxplot")
        parser.add_argument('-rot', '--label_rotation', type=str, help="Rotate the x-axis labels of the boxplot")
        parser.add_argument('-width', '--width', type=float, help="width of png file")
        parser.add_argument('-height', '--height', type=float, help="height of png file")
        args=parser.parse_args()
        HEIGHT=args.height
        WIDTH=args.width
        DATA=args.data
        LOC=args.location
        GRID=args.gridlines
        FONT=args.fontsize
        ROT=args.label_rotation
        return DATA, LOC, GRID, FONT, ROT, WIDTH, HEIGHT

DATA, LOC, GRID, FONT, ROT, WIDTH, HEIGHT= get_args()

#Move into working directory
os.chdir(LOC)

#Read in dataframe
data = open(LOC+DATA)
df = pd.read_csv(data)


#Create boxplot
boxplot = df.boxplot(fontsize=FONT, rot=ROT, grid=False, figsize=(WIDTH,HEIGHT))

#Save boxplot to png
plt.savefig('boxplot.png')

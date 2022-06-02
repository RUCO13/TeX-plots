import numpy as np
import sys
import subprocess, os

with open('simple-plot.tex','r') as splot:
    text = splot.read()
    text_new = text.replace('data1','test-data.dat')

    with open('simple-plot-new.tex', 'w') as output:
        output.write(text_new)

    
os.system("pdflatex -shell-escape -file-line-error -output-directory=build-ruco %s"%("simple-plot-new.tex"))
os.system("rm -R simple-plot-new.tex")
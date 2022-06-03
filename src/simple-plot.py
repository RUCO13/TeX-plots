import numpy as np
import sys
import subprocess, os



kv = {'data':'../notebooks/data/test-data.dat',
      'xlabel-user':'$x$',
      'ylabel-user':'$y$',
      'legen-user':'first plot',
      'color-user':'blue'}

with open('simple-plot.tex','r') as splot:
    text = splot.read()
    for key, value in kv.items():
        text = text.replace(key, value)
    with open('simple-plot-new.tex', 'w') as output:
        output.write(text)

    
os.system("pdflatex -shell-escape -file-line-error -output-directory=build-ruco %s"%("simple-plot-new.tex"))
os.system("rm -R simple-plot-new.tex")
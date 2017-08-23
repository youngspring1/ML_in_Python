__author__ = 'mike-bowles'

#import urllib2
import urllib.request
import numpy
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.externals.six import StringIO
from math import sqrt
import matplotlib.pyplot as plot

#read data into iterable
target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
#data = urllib2.urlopen(target_url)
data = urllib.request.urlopen(target_url)
datastr = data.read().decode(encoding="utf-8")
datas = datastr.split('\n')
datas.pop()

xList = []
labels = []
names = []
firstLine = True
for line in datas:
    if firstLine:
        names = line.strip().split(";")
        firstLine = False
    else:
        #split on semi-colon
        row = line.strip().split(";")
        #put labels in separate array
        labels.append(float(row[-1]))
        #remove label from row
        row.pop()
        #convert row to floats
        floatRow = [float(num) for num in row]
        xList.append(floatRow)

nrows = len(xList)
ncols = len(xList[0])

wineTree = DecisionTreeRegressor(max_depth=3)

wineTree.fit(xList, labels)

with open("wineTree.dot", 'w') as f:
    f = tree.export_graphviz(wineTree, out_file=f)
#Note: The code above exports the trained tree info to a Graphviz "dot" file.
#Drawing the graph requires installing GraphViz and the running the following on the command line
#dot -Tpng wineTree.dot -o wineTree.png


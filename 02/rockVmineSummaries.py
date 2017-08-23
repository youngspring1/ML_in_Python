__author__ = 'mike_bowles'
#import urllib2
import urllib.request
import sys
import requests

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#data = urllib2.urlopen(target_url)
data = urllib.request.urlopen(target_url)
print(type(data))#<class 'http.client.HTTPResponse'>
#data = str(data.read())
datastr = data.read().decode(encoding="utf-8")
#print(datastr)
datas = datastr.split('\n')
print(type(datas))
print(len(datas))

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in datas:
    #print(line)
    if not line == "":
        #split on comma
        row = line.strip().split(",")
        xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])) + '\n')


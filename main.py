import os
import plotly.figure_factory as pff
import statistics as st
import pandas as pd
import random
import plotly.graph_objects as pgo

os.system('cls')

f = open('studentMarks.csv')

df = pd.read_csv('studentMarks.csv')

data = df['Math_score'].to_list()

pMean = st.mean(data)
pStd = st.stdev(data)

#print(pMean,pStd)

graph = pff.create_distplot([data], ['Math_score'], show_hist=False)

# graph.show()


def DataPoints():
    rData = []

    for i in range(101):
        p = random.randint(0, len(data)-1)
        value = data[p]
        rData.append(value)

    rMean = st.mean(rData)

    return rMean


Mlist = []

for i in range(1001):
    DpMean = DataPoints()
    Mlist.append(DpMean)

graph2 = pff.create_distplot([Mlist], ['Math_score'], show_hist=False)
#graph2.show()

sMean = st.mean(Mlist)
sStd = st.stdev(Mlist)

#print(sMean,sStd)

#1std 2std 3std

fstds = (pMean-sStd)
fstde = (pMean+sStd)

sstds = (pMean-2*sStd)
sstde = (pMean+2*sStd)

tstds = (pMean-3*sStd)
tstde = (pMean+3*sStd)

#data 1
f1 = open('data1.csv')
df1 = pd.read_csv('data1.csv')
data1 = df['Math_score'].to_list()
data1M = st.mean(data1)
graphd1 = pff.create_distplot([Mlist], ['Math_score'], show_hist=False)
graphd1.add_trace(pgo.Scatter(x=[data1M,data1M],y=[0,0.1],mode='lines',name='Data1Mean'))
graphd1.add_trace(pgo.Scatter(x=[fstde,fstde],y=[0,0.1],mode='lines',name='1STD'))
#graphd1.show()

#data 2
f2 = open('data2.csv')
df2 = pd.read_csv('data2.csv')
data2 = df['Math_score'].to_list()
data2M = st.mean(data2)
graphd2 = pff.create_distplot([Mlist], ['Math_score'], show_hist=False)
graphd2.add_trace(pgo.Scatter(x=[data2M,data2M],y=[0,0.1],mode='lines',name='Data2Mean'))
graphd2.add_trace(pgo.Scatter(x=[fstde,fstde],y=[0,0.1],mode='lines',name='1STD'))
graphd2.add_trace(pgo.Scatter(x=[sstde,sstde],y=[0,0.1],mode='lines',name='sSTD'))
#graphd2.show()

#data 3
f3 = open('data3.csv')
df3 = pd.read_csv('data3.csv')
data3 = df['Math_score'].tolist()
data3M = st.mean(data3)
graphd3 = pff.create_distplot([Mlist], ['Math_score'], show_hist=False)
graphd3.add_trace(pgo.Scatter(x=[data3M,data3M],y=[0,0.1],mode='lines',name='Data3Mean'))
graphd3.add_trace(pgo.Scatter(x=[fstde,fstde],y=[0,0.1],mode='lines',name='1STD'))
graphd3.add_trace(pgo.Scatter(x=[sstde,sstde],y=[0,0.1],mode='lines',name='2STD'))
graphd3.add_trace(pgo.Scatter(x=[tstde,tstde],y=[0,0.1],mode='lines',name='3STD'))
graphd3.show()
print(data3M)

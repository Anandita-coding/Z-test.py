import pandas as pd 
import plotly.figure_factory as ff
import statistics
import random 
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
sd = statistics.stdev(data)
print("The mean of the population is", mean)
print("The Standard Deviation of the population is ",sd)

fig = ff.create_distplot([data],["Result"],show_hist = False)
fig.show() 

firstsdstart = 0
firstsdend =0
secondsdstart =0
secondsdend = 0
thirdsdstart =0
thirdsdend = 0

def randomSetofMeans(counter):
  randomSamples = []

  for i in range(0,counter):
    index = random.randint(0,len(data)-1)
    value = data[index]
    randomSamples.append(value)

  mean = statistics.mean(randomSamples)

  return mean

def showFigure(randomSamples):
  mean = statistics.mean(randomSamples)
  sd = statistics.stdev(randomSamples)
  print("The mean of the sample is ", mean)
  print("The Standard deviation of the sample is ", sd)

  firstsdstart = mean -sd
  firstsdend = mean+sd
  secondsdstart = mean-sd*2
  secondsdend = mean +sd*2
  thirdsdstart = mean-sd*3
  thirdsdend = mean+sd*3

  fig = ff.create_distplot([randomSamples],["result"], show_hist = False)
  fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.4], mode = "lines", name = "Mean"))
  fig.add_trace(go.Scatter(x = [firstsdstart,firstsdstart], y = [0,0.4], mode = "lines", name = "SD1 start"))
  fig.add_trace(go.Scatter(x = [secondsdstart,secondsdstart], y = [0,0.4], mode = "lines", name = "SD2 start"))
  fig.add_trace(go.Scatter(x = [thirdsdstart,thirdsdstart], y = [0,0.4], mode = "lines", name = "SD3 start"))
  fig.add_trace(go.Scatter(x = [firstsdend,firstsdend], y = [0,0.4], mode = "lines", name = "SD1 end"))
  fig.add_trace(go.Scatter(x = [secondsdend,secondsdend], y = [0,0.4], mode = "lines", name = "SD2 end"))
  fig.add_trace(go.Scatter(x = [thirdsdend,thirdsdend], y = [0,0.4], mode = "lines", name = "SD3 end"))
  fig.show()

def main():
  meanList = []

  for i in range(0,1000):
    setOfMean = randomSetofMeans(100)
    meanList.append(setOfMean)

  showFigure(meanList)
main()

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

mean1 = statistics.mean(data)
print("The mean of the dataset1 is", mean1)


fig = ff.create_distplot([data],["Result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.04], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [firstsdstart,firstsdstart], y = [0,0.04], mode = "lines", name = "SD1 start"))
fig.add_trace(go.Scatter(x = [secondsdstart,secondsdstart], y = [0,0.04], mode = "lines", name = "SD2 start"))
fig.add_trace(go.Scatter(x = [thirdsdstart,thirdsdstart], y = [0,0.04], mode = "lines", name = "SD3 start"))
fig.add_trace(go.Scatter(x = [firstsdend,firstsdend], y = [0,0.04], mode = "lines", name = "SD1 end"))
fig.add_trace(go.Scatter(x = [secondsdend,secondsdend], y = [0,0.04], mode = "lines", name = "SD2 end"))
fig.add_trace(go.Scatter(x = [thirdsdend,thirdsdend], y = [0,0.04], mode = "lines", name = "SD3 end"))
fig.add_trace(go.Scatter(x = [mean1,mean1], y = [0,0.04], mode = "lines", name = "Mean of Intervention 1"))
fig.show()

ztest = (mean1-mean)/2.051090293305317
print(ztest)

df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()

mean2 = statistics.mean(data)
print("The mean of the dataset1 is", mean2)


fig = ff.create_distplot([data],["Result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.04], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [firstsdstart,firstsdstart], y = [0,0.04], mode = "lines", name = "SD1 start"))
fig.add_trace(go.Scatter(x = [secondsdstart,secondsdstart], y = [0,0.04], mode = "lines", name = "SD2 start"))
fig.add_trace(go.Scatter(x = [thirdsdstart,thirdsdstart], y = [0,0.04], mode = "lines", name = "SD3 start"))
fig.add_trace(go.Scatter(x = [firstsdend,firstsdend], y = [0,0.04], mode = "lines", name = "SD1 end"))
fig.add_trace(go.Scatter(x = [secondsdend,secondsdend], y = [0,0.04], mode = "lines", name = "SD2 end"))
fig.add_trace(go.Scatter(x = [thirdsdend,thirdsdend], y = [0,0.04], mode = "lines", name = "SD3 end"))
fig.add_trace(go.Scatter(x = [mean2,mean2], y = [0,0.04], mode = "lines", name = "Mean of Intervention 2"))
fig.show()

ztest = (mean2-mean)/sd
print(ztest)

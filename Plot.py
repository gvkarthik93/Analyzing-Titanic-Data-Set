import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generateBarGraph(metrics, title, xLabel):
	objects = ('Male', 'Female')
	y_pos = np.arange(len(objects))

	braGraph = plt.bar(y_pos, metrics, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	braGraph[0].set_color('b')
	braGraph[1].set_color('g')
	plt.ylabel('Number of children survived')
	plt.xlabel(xLabel)
	plt.title(title)
	plt.show()

df = pd.read_csv('/Users/karthik/Development/Analyzing-Titanic-Data-Set/titanic.csv')

df.drop(df.columns[[0]], axis=1)
rowsData = df.shape[0]

maleCount = 0
femaleCount = 0
mA = 0 
mB = 0
mC = 0
fA = 0
fB = 0
fC = 0

for x in range(0,df.shape[0]):
	if int(df["Age"][x]) < 13 and int(df["Sex"][x]) == 1 and int(df["Survived"][x]) == 1:
		maleCount = maleCount + 1
		if int(df["Pclass"][x]) == 1:
			mA = mA + 1
		if int(df["Pclass"][x]) == 2:
			mB = mB + 1
		if int(df["Pclass"][x]) == 3:
			mC = mC + 1

	elif int(df["Age"][x]) < 13 and int(df["Sex"][x]) == 0 and int(df["Survived"][x]) == 1:
		femaleCount = femaleCount + 1
		if int(df["Pclass"][x]) == 1:
			fA = fA + 1
		if int(df["Pclass"][x]) == 2:
			fB = fB + 1
		if int(df["Pclass"][x]) == 3:
			fC = fC + 1

# Get from the data set
survivalCount = [maleCount,femaleCount]
classASurvivalCount = [mA,fA]
classBSurvivalCount = [mB,fB]
classCSurvivalCount = [mC,fC]
generateBarGraph(survivalCount, "Total number of children survived", "Gender")
generateBarGraph(classASurvivalCount, "Class A children", "Gender")
generateBarGraph(classBSurvivalCount, "Class B children", "Gender")
generateBarGraph(classCSurvivalCount, "Class C children", "Gender")

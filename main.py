import matplotlib.pyplot as mt
from matplotlib.ticker import MultipleLocator
import numpy as np
from setpy import spmean

directory_str = "datasets/"
spm = spmean(directory_str)
covidArr = spm.dataMean("01/08/2020", "03/12/2020", "03/13/2020", "04/13/2020")

# Graphing Data

def maxAvg(arr1, arr2):
    if max(arr1) > max(arr2):
        return max(arr1)
    else:
        return max(arr2)

width = 0.35
y_pos = np.arange(len(spm.names))
preCov = mt.bar(y_pos - width/2, covidArr[0], width, label='Pre-Covid')
cov = mt.bar(y_pos + width/2, covidArr[1], width, label='Covid')
# mt.bar(y_pos, avgarr)

mt.xticks(y_pos, spm.names)
mt.yticks(np.arange(0, maxAvg(covidArr[0], covidArr[1])+1, 1.0))
mt.axes().yaxis.set_minor_locator(MultipleLocator(0.5))
mt.xlabel("Counties")
mt.ylabel("NO2 Levels (ppb)")
mt.title('New York Counties NO2 Daily Levels')
mt.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    # autolabel() Code by MatPlotLib.
    for rect in rects:
        height = round(rect.get_height(), 2)
        mt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(preCov)
autolabel(cov)
mt.show()

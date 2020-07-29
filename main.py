import matplotlib.pyplot as mt
from matplotlib.ticker import MultipleLocator
import numpy as np

preCovArr = []
covArr = []
names = ['Erie', 'Queens', 'Bronx', 'Monroe']

def dataMean(data, covActive):
    with open(data, 'r+') as f:
        text = f.read()
        text = text.replace("\"", "")
        f.seek(0)
        f.write(text)
        f.truncate()
    data_file = np.loadtxt(data, dtype=str, delimiter=',')
    pol = data_file[:, 4]
    avgArr = []
    # Searches 3/13/2020 - 04/21/2020
    # Searches within 01/08/2020 - 03/12/2020
    if (covActive):
        for i in range(len(data_file)):
            if (np.char.replace(data_file[i,0], "/","").astype(np.float) > 3122020 and np.char.replace(data_file[i,0], "/","").astype(np.float) > 4012020):
                avgArr.append(data_file[i, 4])
    else:
        for i in range(len(data_file)):
            if (np.char.replace(data_file[i,0], "/","").astype(np.float) < 3132020 and np.char.replace(data_file[i,0], "/","").astype(np.float) > 1082020):
                avgArr.append(data_file[i, 4])
        #for x in pol:

    pol = np.array(pol).astype(np.float)

    avg = np.mean(np.array(avgArr).astype(np.float), dtype=float)
    if (covActive):
        covArr.append(avg)

    else:
        preCovArr.append(avg)


def maxAvg(arr1, arr2):
    if max(arr1) > max(arr2):
        return max(arr1)
    else:
        return max(arr2)

dataMean('erie.txt', False)
dataMean('erie.txt', True)
dataMean('queens.txt', False)
dataMean('queens.txt', True)
dataMean('bronx.txt', False)
dataMean('bronx.txt', True)
dataMean('monroe.txt', False)
dataMean('monroe.txt', True)

# Graphing Data
width = 0.35

y_pos = np.arange(len(names))
preCov = mt.bar(y_pos - width/2, preCovArr, width, label='Pre-Covid')
cov = mt.bar(y_pos + width/2, covArr, width, label='Covid')
# mt.bar(y_pos, avgarr)

mt.xticks(y_pos, names)
mt.yticks(np.arange(0, maxAvg(preCovArr, covArr)+1, 1.0))
mt.axes().yaxis.set_minor_locator(MultipleLocator(0.5))
mt.xlabel("Counties")
mt.ylabel("NO2 Levels (ppb)")
mt.title('New York Counties NO2 Daily Levels')
mt.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
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

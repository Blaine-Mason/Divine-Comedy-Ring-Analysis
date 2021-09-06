import numpy as np
import pandas as pd


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


df = pd.read_table('inferno.txt',header=None)
line_nums = list(df[0].str.extractall(r"(Inferno . Canto .{1,6})")[0].index)
for i in range(0,len(line_nums)):
    line_nums[i] = line_nums[i][0]
line_nums.append(len(df))


inferno = pd.DataFrame(index=[f"Canto-{x}" for x in range(1,35)], columns=["Lines"])
cantos = [f"Canto-{x}" for x in range(1,35)]


i = 1
for c in cantos:
    inferno.at[c, "Lines"] = list(df[0][line_nums[i-1]+1:line_nums[i]])
    i = i + 1


#Parse is c_ = " ".join(inferno.loc["Canto-_"]["Lines"])
canto = " ".join(inferno.loc[c]["Lines"])


sort_orders = sorted(word_count(canto).items(), key=lambda x: x[1], reverse=True)


i = 1
for c in cantos:
    canto = " ".join(inferno.loc[c]["Lines"])
    inferno.at[c, "Lines"] = sorted(word_count(canto).items(), key=lambda x: x[1], reverse=True)
    i = i + 1


temp = inferno.loc["Canto-1"]["Lines"]


x = np.array([temp[i][0] for i in range(0, len(temp))])
y = np.array([int(temp[i][1]) for i in range(0, len(temp))])


inferno




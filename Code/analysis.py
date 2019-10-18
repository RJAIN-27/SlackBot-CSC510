import pandas as pd
from scipy.stats import shapiro
from tabulate import tabulate
from datetime import datetime

def analysis(path, target):
    # create file
    now = datetime.now()
    dt_string = "analysis_"+now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    f = open(dt_string, "w")

    # Exploratory data analysis:
    f.writelines("EXPLORATORY DATA ANALYSIS")
    f.writelines("\nCorrelation")


    data = pd.read_csv(path, sep=',', header=0)

    f.writelines("\nShapiro-Wilk test - normal distribution test\n")
    ls = []
    columns = list(data.columns)
    for i in columns:
        if i == target:
            continue
        stat, p = shapiro(data[i])
        if p>0.05:
            result = "Accepted"
        else:
            result = "Rejected"
        ls.append([i,stat,p,result])
    dataf = pd.DataFrame(ls, columns = ["Column","Test Statistics","p-Value","Null Hypothesis"])
    f.write(tabulate(dataf, tablefmt="grid", headers="keys", showindex=False))

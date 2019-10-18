import pandas as pd
from scipy.stats import shapiro
from tabulate import tabulate
from datetime import datetime

def analysis(path, target):
    # create file
    now = datetime.now()
    dt_string = "analysis_"+now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    f = open(dt_string, "w")
    data = pd.read_csv(path, sep=',', header=0)
    columns = list(data.columns)

    # Exploratory data analysis:
    f.writelines("\nEXPLORATORY DATA ANALYSIS:")

    # number of null values per column
    f.writelines("\n\nNo. of nulls in the columns:\n")
    f.write(str(data.isnull().sum()))

    # Correlation
    f.writelines("\n\nCorrelation:\n")
    correlations = data[data.columns].corr(method='pearson')
    for i in range(len(columns)-1):
        for j in range(i+1, len(columns)):
            if abs(correlations[columns[i]][columns[j]])<0.5:
              f.writelines("\nColumns "+columns[i]+" and "+columns[j] +" have low correlation between them. The correlation value is "+str(correlations[columns[i]][columns[j]]))
            elif abs(correlations[columns[i]][columns[j]])>0.98:
              f.writelines("\nColumns "+columns[i]+" and "+columns[j] +" have very high correlation between them. The correlation value is "+str(correlations[columns[i]][columns[j]]))
            else:
              f.writelines("\nColumns "+columns[i]+" and "+columns[j] +" have strong correlation between them. The correlation value is "+str(correlations[columns[i]][columns[j]]))
    
    # STATISTICS TEST
    # Normal Distribution Test
    f.writelines("\n\nShapiro-Wilk test - normal distribution test\n")
    ls = []

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

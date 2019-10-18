import pandas as pd
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson
from tabulate import tabulate
from datetime import datetime

def correlations(data, method,columns,f):
    correlations = data[data.columns].corr(method=method)
    for i in range(len(columns) - 1):
        for j in range(i + 1, len(columns)):
            if abs(correlations[columns[i]][columns[j]]) < 0.5:
                f.writelines("\nColumns " + columns[i] + " and " + columns[
                    j] + " have low correlation between them. The correlation value is " + str(
                    correlations[columns[i]][columns[j]]))
            elif abs(correlations[columns[i]][columns[j]]) > 0.98:
                f.writelines("\nColumns " + columns[i] + " and " + columns[j] +
                             " have very high correlation between them. The correlation value is " +
                             str(correlations[columns[i]][columns[j]]))
            else:
                f.writelines("\nColumns " + columns[i] + " and " + columns[j] +
                             " have strong correlation between them. The correlation value is "
                             + str(correlations[columns[i]][columns[j]]))

def analysis(path, target):
    # create file
    now = datetime.now()
    dt_string = "analysis_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
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
    f.writelines("\n\nPearson Correlation test:")
    correlations(data,'pearson',columns,f)

    f.writelines("\n\nSpearman's rank Correlation test:")
    correlations(data,'spearman',columns,f)

    f.writelines("\n\nKendall's rank Correlation test:")
    correlations(data, 'kendall', columns, f)

    # Normality Test
    f.writelines("\n\nNormality Tests:")
    # Shapiro-Wilk test
    f.writelines("\nShapiro-Wilk test - Gaussian distribution test\n")
    f.writelines("Tests whether a data sample has a Gaussian distribution.\n")
    f.writelines("Hypothesis: the sample has a Gaussian distribution\n")
    ls = []
    for i in columns:
        if i == target:
            continue
        stat, p = shapiro(data[i])
        if p > 0.05:
            result = "Accepted"
        else:
            result = "Rejected"
        ls.append([i, stat, p, result])
    dataf = pd.DataFrame(ls, columns=["Column", "Test Statistics", "p-Value", "Null Hypothesis"])
    f.write(tabulate(dataf, tablefmt="grid", headers="keys", showindex=False))

    # D’Agostino’s K^2 test
    f.writelines("\n\nD’Agostino’s K^2 Test - Gaussian distribution test\n")
    f.writelines("Tests whether a data sample has a Gaussian distribution.\n")
    f.writelines("Hypothesis: the sample has a Gaussian distribution\n")
    ls = []
    for i in columns:
        if i == target:
            continue
        stat, p = normaltest(data[i])
        if p > 0.05:
            result = "Accepted"
        else:
            result = "Rejected"
        ls.append([i, stat, p, result])
    dataf = pd.DataFrame(ls, columns=["Column", "Test Statistics", "p-Value", "Null Hypothesis"])
    f.write(tabulate(dataf, tablefmt="grid", headers="keys", showindex=False))

    # Anderson-Darling Test
    f.writelines("\n\nAnderson-Darling Test - Gaussian distribution test\n")
    f.writelines("Tests whether a data sample has a Gaussian distribution.\n")
    f.writelines("Hypothesis: the sample has a Gaussian distribution\n")
    ls = []
    for i in columns:
        if i == target:
            continue
        result = anderson(data[i])
        f.writelines('\n'+i+':\nStatistic: '+ str(result.statistic)+'\n')
        p = 0
        for j in range(len(result.critical_values)):
            sl, cv = result.significance_level[j], result.critical_values[j]
            if result.statistic < result.critical_values[j]:
                f.writelines(str(sl)+':'+str(cv) +' Null Hypothesis - Accepted\n')
            else:
                f.writelines(str(sl)+':'+str(cv) +' Null Hypothesis - Rejected\n')

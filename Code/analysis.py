import pandas as pd
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson

from tabulate import tabulate
from datetime import datetime

import numpy as np 
import seaborn as sns 
from scipy.stats import trim_mean

import json
import commonFunctions
       
# FUNCTION TO FIND CORRELATION BETWEEN ALL VARIABLES IN THE DATASET     
def correlations(data, method, columns, f):
    correlations = data[data.columns].corr(method=method)
    for i in range(len(columns) - 1):
        for j in range(i + 1, len(columns)):
            if abs(correlations[columns[i]][columns[j]]) < 0.5:
                f.writelines("\nColumns " + columns[i] + " and " + columns[j] +
                             " have low correlation between them. The correlation value is " +
                             str(correlations[columns[i]][columns[j]]))
            elif abs(correlations[columns[i]][columns[j]]) > 0.98:
                f.writelines("\nColumns " + columns[i] + " and " + columns[j] +
                             " have very high correlation between them. The correlation value is " +
                             str(correlations[columns[i]][columns[j]]))
            else:
                f.writelines("\nColumns " + columns[i] + " and " + columns[j] +
                             " have strong correlation between them. The correlation value is "
                             + str(correlations[columns[i]][columns[j]]))
    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")

    
#FUNCTION TO WRITE ALL EDA RESULTS TO FILE AND RETURN FILE  
def analysis(f, data, target, columns, dt_string):

    # Exploratory data analysis:
    f.writelines("\nEXPLORATORY DATA ANALYSIS:")
    
    # Details about the datset
    dataInfo(f, data, target, columns, dt_string)
    
    #Mean, Median and Mode
    MeanMedianMode(f, data, target, columns, dt_string)
    
    # Correlation
    f.writelines("\n\nCorrelation:\n")
    f.writelines("\nPearson Correlation test:")
    correlations(data, 'pearson', columns, f)

    f.writelines("\n\nSpearman's rank Correlation test:")
    correlations(data, 'spearman', columns, f)

    f.writelines("\n\nKendall's rank Correlation test:")
    correlations(data, 'kendall', columns, f)
    
    #Normality Tests
    Normality(f, data, target, columns, dt_string)
    
    return dt_string


#FUNCTION TO DISPLAY INFORMATION ABOUT DATASET 
def dataInfo(f, data, target, columns, dt_string):
    # number of null values per column
    f.writelines("\n\nNo. of nulls in the columns:\n")
    f.write(str(data.isnull().sum()))
    # Information about the data: 
    f.writelines("\nInformation about the data:")
    f.writelines("\n\nType of the data: "+str(type(data)))
    f.writelines("\n\nSummary statistics of the data\n\n")
    f.writelines(str(data.describe()))
    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")
     

#FUNCTION TO FIND MEAN, MEDIAN, MODE OF EVERY COLUMN
def MeanMedianMode(f, data, target, columns, dt_string):
    # Mean, median and mode of each column:
    f.writelines("\n\nMEAN, MEDIAN AND MODE:")
    for col in columns:
        f.writelines("\n" + col)
        f.writelines("\nMean= " + str(data[col].mean()))
        f.writelines("     Median= " + str(data[col].median()))
        f.writelines("     Mode= " + str(mode) for mode in data[col].mode())
    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")
    #return dt_string

#FUNCTION TO TEST NORMALITY OF THE DATASET
def Normality(f, data, target, columns, dt_string):    
    # Normality Test
    f.writelines("\n\nNormality Tests:")
    # Shapiro-Wilk test
    ShapiroWilkTest(f, data, target, columns, dt_string)
    #D'Agostino's K^2 Test 
    Agostino(f, data, target, columns, dt_string)
    #Anderson-Darling Test
    AndersonDarlingTest(f, data, target, columns, dt_string)
    
def ShapiroWilkTest(f, data, target, columns, dt_string):
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
    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")
    #return dt_string
    
def Agostino(f, data, target, columns, dt_string):    
    f.writelines("\n\nD'Agostino's K^2 Test - Gaussian distribution test\n")
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
    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")
    #return dt_string


def AndersonDarlingTest(f, data, target, columns, dt_string):
    f.writelines("\n\nAnderson-Darling Test - Gaussian distribution test\n")
    f.writelines("Tests whether a data sample has a Gaussian distribution.\n")
    f.writelines("Hypothesis: the sample has a Gaussian distribution\n")
    for i in columns:
        if i == target:
            continue
        result = anderson(data[i])
        f.writelines('\n' + i + ':\nStatistic: ' + str(result.statistic) + '\n')
        for j in range(len(result.critical_values)):
            sl, cv = result.significance_level[j], result.critical_values[j]
            if result.statistic < result.critical_values[j]:
                f.writelines(str(sl) + ':' + str(cv) + ' Null Hypothesis - Accepted\n')
            else:
                f.writelines(str(sl) + ':' + str(cv) + ' Null Hypothesis - Rejected\n')

    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")
    #return dt_string


#FUNCTION TO DISPLAY INFORMATION ABOUT DATASET 
def dataInfo(f, data, target, columns, dt_string):
    # number of null values per column
    f.writelines("\n\nNo. of nulls in the columns:\n")
    f.write(str(data.isnull().sum()))
    # Information about the data: 
    f.writelines("\nInformation about the data:")
    f.writelines("\n\nType of the data: "+str(type(data)))
    f.writelines("\n\nSummary statistics of the data\n\n")
    f.writelines(str(data.describe()))
    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")
     

#FUNCTION TO FIND MEAN, MEDIAN, MODE OF EVERY COLUMN
def MeanMedianMode(f, data, target, columns, dt_string):
    # Mean, median and mode of each column:
    f.writelines("\n\nMEAN, MEDIAN AND MODE:")
    for col in columns:
        f.writelines("\n" + col)
        f.writelines("\nMean= " + str(data[col].mean()))
        f.writelines("     Median= " + str(data[col].median()))
        f.writelines("     Mode= " + str(mode) for mode in data[col].mode())
    f.writelines(
        "\n---------------------------------------------------------------------------------------------------------------------------------------")
    #return dt_string

def analysisInteraction(path,target):
    now = datetime.now()
    dt_string = "analysis_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    f = open(dt_string, "w")
    data = pd.read_csv(path, sep=',', header=0)
    columns = list(data.columns)
    data = data[[col for col in data if data[col].nunique() > 1]]
    columns = list(data.columns)
    flag = commonFunctions.targetCheck(target, columns)
    if flag != 1:
        return flag,[],0
    data,columns,cat_flag = commonFunctions.checkAndConvertIfCategorical(data, target)
    if cat_flag == 0:
        f.writelines("\n      The dataset is of type - Numerical")
    else:
        f.writelines("\n      The dataset is of type - Categorical")
    
    filename = analysis(f,data,target,columns,dt_string)
    f.close()
    return filename

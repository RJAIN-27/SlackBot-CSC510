import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import logging
import operator
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
import commonFunctions as cf
import json

def bestModel(modelDict):
    if len(modelDict)==0:
        return ["No models satisfy this dataset"]
    accr = 70
    models = []
    for model in modelDict:
        if accr<=modelDict[model]:
            accr = modelDict[model]
    for model in modelDict:
        if accr == modelDict[model]:
            models.append(model)

def modelTraining(data, target, column_names):
    # read data
    models={}
    column_names.pop(column_names.index(target))
    X = data.reindex(columns = column_names)
    X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))

    # Assign the target column to a variable
    Y = data[target]

    # Split the datase into training and testing dataset
    X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(X, Y, data.index, test_size=0.2, random_state=0)
    # Linear SVC
    try:
        lsvc = LinearSVC()
        y_pred = lsvc.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Linear Support Vector Classifier"] = model_accr
    except:
        logging.info("LSVC is throwing exception")

    # KNN
    try:
        knn = KNeighborsClassifier()
        y_pred = knn.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["KNN Classifier"] = model_accr
    except:
        logging.info("KNN is throwing exception")

    # DTC
    try:
        clf_gini = DecisionTreeClassifier(criterion="gini", random_state=0)
        y_pred = clf_gini.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Decision Tree Classifier - GINI"] = model_accr
    except:
        logging.info("DTC GINI is throwing exception")

    try:
        clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=0)
        y_pred = clf_entropy.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Decision Tree Classifier - ENTROPY"] = model_accr
    except:
        logging.info("DTC ENTROPY is throwing exception")

    # Multinomial NB
    try:
        mnb_model = MultinomialNB()
        y_pred = mnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Multinomial Naive Bayes"]=model_accr
    except:
        logging.info("Multinomial NB is throwing exception")

    # Bernoulli NB
    try:
        bnb_model = BernoulliNB()
        y_pred = bnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Bernoulli Naive Bayes"] = model_accr
    except:
        logging.info("Bernoulli NB is throwing exception")

    # Gaussian NB
    try:
        gnb_model = GaussianNB()
        y_pred = gnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Gaussian Naive Bayes"] = model_accr
    except:
        logging.info("GaussianNB is throwing exception")

    # ADB
    try:
        adb = AdaBoostClassifier(n_estimators=200, learning_rate=1)
        # Train Adaboost Classifer
        y_pred =adb.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["AdaBoost Classifier"] = model_accr
    except:
        logging.info("AdaBoost Classifier is throwing exception")

    #XGB
    try:
        xgb = XGBClassifier()
        y_pred = xgb.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["XGB Classifier"] = model_accr
    except:
        logging.info("XGB Classifier is throwing exception")

    # Random Forest Classifier
    try:
        rfc = RandomForestClassifier(n_estimators=100)
        y_pred = rfc.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Random Forest Classifier"]=model_accr
    except:
        logging.info("Random Forest Classifier is throwing exception")

    return(models)

def modelSelInteraction(path,target):
    data = pd.read_csv(path, sep=',', header=0)

    # remove the columns which have no unique elements
    data = data[[col for col in data if data[col].nunique() > 1]]
    column_names = list(data.columns)
    flag = cf.targetCheck(target, column_names)
    if flag != 1:
        return flag
    data = cf.checkAndConvertIfCategorical(data,target)
    models = modelTraining(data,target,column_names)
    return bestModel(models)

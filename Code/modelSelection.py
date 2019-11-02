import logging
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

def bestModel(modelDict,f):
    if len(modelDict)==0:
        f.writelines("\n      No model to satisfy this dataset")
        return ["No model to satisfy this dataset"]
    accr = 70
    models = []
    for model in modelDict:
        if accr<=modelDict[model]:
            accr = modelDict[model]
    for model in modelDict:
        if accr == modelDict[model]:
            models.append(model)

    return models if len(models)>0 else ["No decent model to satisfy this dataset"]

def modelTraining(X_train, X_test, y_train, y_test,f):
    models = {}
    # Linear SVC
    try:
        lsvc = LinearSVC()
        y_pred = lsvc.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Linear Support Vector Classifier"] = model_accr
        f.writelines("\n      Accuracy of Linear Support Vector Classifier is " + str(model_accr))
    except:
        logging.info("LSVC is throwing exception")
        f.writelines("\n      LSVC is throwing exception")

    # KNN
    try:
        knn = KNeighborsClassifier()
        y_pred = knn.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["KNN Classifier"] = model_accr
        f.writelines("\n      Accuracy of KNN Classifier is " + str(model_accr))
    except:
        logging.info("KNN is throwing exception")
        f.writelines("\n      KNN is throwing exception")

    # DTC
    try:
        clf_gini = DecisionTreeClassifier(criterion="gini", random_state=0)
        y_pred = clf_gini.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Decision Tree Classifier - GINI"] = model_accr
        f.writelines("\n      Accuracy of Decision Tree Classifier - GINI is " + str(model_accr))
    except:
        logging.info("DTC GINI is throwing exception")
        f.writelines("\n      DTC GINI is throwing exception")

    try:
        clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=0)
        y_pred = clf_entropy.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Decision Tree Classifier - ENTROPY"] = model_accr
        f.writelines("\n      Accuracy of Decision Tree Classifier - ENTROPY is " + str(model_accr))
    except:
        logging.info("DTC ENTROPY is throwing exception")
        f.writelines("\n      DTC ENTROPY is throwing exception")

    # Multinomial NB
    try:
        mnb_model = MultinomialNB()
        y_pred = mnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Multinomial Naive Bayes"] = model_accr
        f.writelines("\n      Accuracy of Multinomial NB is " + str(model_accr))
    except:
        logging.info("Multinomial NB is throwing exception")
        f.writelines("\n      Multinomial NB is throwing exception")

    # Bernoulli NB
    try:
        bnb_model = BernoulliNB()
        y_pred = bnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Bernoulli Naive Bayes"] = model_accr
        f.writelines("\n      Accuracy of Bernoulli NB is " + str(model_accr))
    except:
        logging.info("Bernoulli NB is throwing exception")
        f.writelines("\n      Bernoulli NB is throwing exception")

    # Gaussian NB
    try:
        gnb_model = GaussianNB()
        y_pred = gnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Gaussian Naive Bayes"] = model_accr
        f.writelines("\n      Accuracy of GaussianNB is " + str(model_accr))
    except:
        logging.info("GaussianNB is throwing exception")
        f.writelines("\n      GaussianNB is throwing exception")

    # ADB
    try:
        adb = AdaBoostClassifier(n_estimators=200, learning_rate=1)
        # Train Adaboost Classifer
        y_pred = adb.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["AdaBoost Classifier"] = model_accr
        f.writelines("\n      Accuracy of AdaBoost Classifier is " + str(model_accr))
    except:
        logging.info("AdaBoost Classifier is throwing exception")
        f.writelines("\n      AdaBoost Classifier is throwing exception")

    # XGB
    try:
        xgb = XGBClassifier()
        y_pred = xgb.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["XGB Classifier"] = model_accr
        f.writelines("\n      Accuracy of XGB Classifier is " + str(model_accr))
    except:
        logging.info("XGB Classifier is throwing exception")
        f.writelines("\n      XGB Classifier is throwing exception")

    # Random Forest Classifier
    try:
        rfc = RandomForestClassifier(n_estimators=100)
        y_pred = rfc.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        models["Random Forest Classifier"] = model_accr
        f.writelines("\n      Accuracy of Random Forest Classifier is " + str(model_accr))
    except:
        logging.info("Random Forest Classifier is throwing exception")
        f.writelines("\n      Random Forest Classifier is throwing exception")

    return (models)

def prepAndSplit1(data, target, column_names, f):
    # read data
    column_names.pop(column_names.index(target))
    f.writelines("\nStep 3: Spliting the target column from the dataset")
    X = data.reindex(columns = column_names)
    X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
    f.writelines("\nStep 4: Preprocessing using sklearn package")

    # Assign the target column to a variable
    Y = data[target]

    # Split the datase into training and testing dataset
    f.writelines("\nStep 5: Spliting the training and testing data in 80:20 ratio")
    X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(X, Y, data.index, test_size=0.2, random_state=0)
    return X_train,X_test,y_train,y_test

def prepAndSplit2(data,target,column_names,f):
    column_names.pop(column_names.index(target))
    X = data.reindex(columns=column_names)
    Y = data[target]
    X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(X, Y, data.index, test_size=0.2,
                                                                                     random_state=0)
    return X_train, X_test, y_train, y_test

def modelSelInteraction(path,target):
    data, column_names, cat_flag = cf.preprocessS1(path,target)
    if column_names==[]:
        return data
    f = open("modelSelectionProcess.txt", "w")
    f.writelines(
        "\nThe following is the process the bot performed to arrived at the best model for the provided dataset.")
    f.writelines("\n***************************MODEL SELECTION PROCESS**********************")
    f.writelines("\nThe file name is: "+str(path.split("/")[-1]))
    f.writelines("\nStep 1: Check if the target is present in the column names of the dataset")
    f.writelines("\nStep 2: Check if the columns are numerical or categorical. If categorical, factorize.")
    if cat_flag == 0:
        f.writelines("\n      The dataset is of type - Numerical")
    else:
        f.writelines("\n      The dataset is of type - Categorical")
        target = target+"id"
    f.writelines("\n      The dataset contains column names (after pre-processing stage 1): "+str(column_names))
    f.writelines(data.head())
    X_train, X_test, y_train, y_test = prepAndSplit1(data,target,column_names,f)
    f.writelines("\nStep 6: Training and testing with various models")
    models = modelTraining(X_train, X_test, y_train, y_test, f);
    f.writelines("\nStep 7: Finding the best model:")
    bestMod = bestModel(models, f)
    if bestMod == ["No decent model to satisfy this dataset"]:
        f.writelines("\n      No decent model to satisfy this dataset. All the accuracies are below 70%")
        if cat_flag==0:
            data2 = cf.ngram(data,target)
            target = target+"ConvertedFeatures"
            X_train, X_test, y_train, y_test = prepAndSplit2(data2, target, column_names, f)
            models = modelTraining(X_train, X_test, y_train, y_test, f);
            f.close()
            return bestModel(models, f)
    else:
        f.writelines("\n      Best Model(s):")
        for i in bestMod:
            f.writelines("\n          "+str(i))
    f.close()
    return bestMod

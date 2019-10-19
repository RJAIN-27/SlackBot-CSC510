import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
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
#from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier

def modelSelection(path, target):
    # read data
    data = pd.read_csv(path, sep=',', header=0)

    # remove the columns which have no unique elements
    data = data[[col for col in data if data[col].nunique() > 1]]
    column_names = list(data.columns)
    column_names.pop(column_names.index(target))
    X = data.reindex(columns = column_names)
    X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))

    # Assign the target column to a variable
    Y = data[target]

    # Split the datase into training and testing dataset
    X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(X, Y, data.index, test_size=0.2,
                                                                                     random_state=0)
    best_model = "none"
    best_accr = 0

    # Linear SVC
    try:
        lsvc = LinearSVC()
        y_pred = lsvc.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr>best_accr:
            best_accr = model_accr
            best_model = "Linear Support Vector Classifier"
    except:
        logging.info("LSVC is throwing exception")

    # KNN
    try:
        knn = KNeighborsClassifier()
        y_pred = knn.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "KNN Classifier"
    except:
        logging.info("KNN is throwing exception")

    # DTC
    try:
        clf_gini = DecisionTreeClassifier(criterion="gini", random_state=0)
        y_pred = clf_gini.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "Decision Tree Classifier - GINI"
    except:
        logging.info("DTC GINI is throwing exception")

    try:
        clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=0)
        y_pred = clf_entropy.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "Decision Tree Classifier - ENTROPY"
    except:
        logging.info("DTC ENTROPY is throwing exception")

    # Multinomial NB
    try:
        mnb_model = MultinomialNB()
        y_pred = mnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "Multinomial Naive Bayes"
    except:
        logging.info("Multinomial NB is throwing exception")

    # Bernoulli NB
    try:
        bnb_model = BernoulliNB()
        y_pred = bnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "Bernoulli Naive Bayes"
    except:
        logging.info("Bernoulli NB is throwing exception")

    # Gaussian NB
    try:
        gnb_model = GaussianNB()
        y_pred = gnb_model.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "Gaussian Naive Bayes"
    except:
        logging.info("GaussianNB is throwing exception")

    # ADB
    try:
        adb = AdaBoostClassifier(n_estimators=200, learning_rate=1)
        # Train Adaboost Classifer
        y_pred =adb.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "AdaBoost Classifier"
    except:
        logging.info("AdaBoost Classifier is throwing exception")

    #XGB
    try:
        xgb = XGBClassifier()
        y_pred = xgb.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "XGB Classifier"
    except:
        logging.info("XGB Classifier is throwing exception")

    # Random Forest Classifier
    try:
        rfc = RandomForestClassifier(n_estimators=100)
        y_pred = rfc.fit(X_train, y_train).predict(X_test)
        model_accr = metrics.accuracy_score(y_test, y_pred) * 100
        if model_accr > best_accr:
            best_accr = model_accr
            best_model = "Random Forest Classifier"
    except:
        logging.info("Random Forest Classifier is throwing exception")

    return(best_model)

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import operator
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
    model_dict = {}  # model and accuracy values

    # Linear SVC
    lsvc = LinearSVC()
    try:
        y_pred_LSVC = lsvc.fit(X_train, y_train).predict(X_test)
        model_dict["Linear Support Vector Classifier"] = metrics.accuracy_score(y_test, y_pred_LSVC) * 100
    except:
        logging.info("LSVC is throwing exception")

    # KNN
    knn = KNeighborsClassifier()
    try:
        y_pred_knn = knn.fit(X_train, y_train).predict(X_test)
        model_dict["KNN Classifier"] = metrics.accuracy_score(y_test, y_pred_knn) * 100
    except:
        logging.info("KNN is throwing exception")

    # DTC
    try:
        clf_gini = DecisionTreeClassifier(criterion="gini", random_state=0)
        y_pred_DTC_gini = clf_gini.fit(X_train, y_train).predict(X_test)
        model_dict["Decision Tree Classifier - GINI"] = metrics.accuracy_score(y_test, y_pred_DTC_gini) * 100
    except:
        logging.info("DTC GINI is throwing exception")

    try:
        clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=0)
        y_pred_DTC_entropy = clf_entropy.fit(X_train, y_train).predict(X_test)
        model_dict["Decision Tree Classifier - ENTROPY"] = metrics.accuracy_score(y_test, y_pred_DTC_entropy) * 100
    except:
        logging.info("DTC ENTROPY is throwing exception")

    # Multinomial NB
    try:
        mnb_model = MultinomialNB()
        y_pred_mnb = mnb_model.fit(X_train, y_train).predict(X_test)
        model_dict["Multinomial Naive Bayes"] = metrics.accuracy_score(y_test, y_pred_mnb) * 100
    except:
        logging.info("Multinomial NB is throwing exception")

    # Bernoulli NB
    try:
        bnb_model = BernoulliNB()
        y_pred_bnb = bnb_model.fit(X_train, y_train).predict(X_test)
        model_dict["Bernoulli Naive Bayes"] = metrics.accuracy_score(y_test, y_pred_bnb) * 100
    except:
        logging.info("Bernoulli NB is throwing exception")

    # Gaussian NB
    try:
        gnb_model = GaussianNB()
        y_pred_gnb = gnb_model.fit(X_train, y_train).predict(X_test)
        model_dict["Gaussian Naive Bayes"] = metrics.accuracy_score(y_test, y_pred_gnb) * 100
    except:
        logging.info("GaussianNB is throwing exception")

    # ADB
    try:
        adb = AdaBoostClassifier(n_estimators=200, learning_rate=1)
        # Train Adaboost Classifer
        y_pred_ada = adb.fit(X_train, y_train).predict(X_test)
        model_dict["AdaBoost Classifier"] = metrics.accuracy_score(y_test, y_pred_ada) * 100
    except:
        logging.info("AdaBoost Classifier is throwing exception")

    #XGB
    try:
        xgb = XGBClassifier()
        y_pred_xgb = xgb.fit(X_train, y_train).predict(X_test)
        model_dict["XG Boost"] = metrics.accuracy_score(y_test, y_pred_xgb) * 100
    except:
        logging.info("XGB Classifier is throwing exception")

    # Random Forest Classifier
    try:
        rfc = RandomForestClassifier(n_estimators=100)
        y_pred_rfc = rfc.fit(X_train, y_train).predict(X_test)
        model_dict["Random Forest Classifier"] = metrics.accuracy_score(y_test, y_pred_rfc) * 100
    except:
        logging.info("Random Forest Classifier is throwing exception")

    model_dict = dict(sorted(model_dict.items(), key=operator.itemgetter(1), reverse=True))

    return list(model_dict.keys())[0]

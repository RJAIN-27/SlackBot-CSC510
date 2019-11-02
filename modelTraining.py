from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import logging

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

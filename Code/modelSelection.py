import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn import metrics
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
  #read data
  data = pd.read_csv(path, sep= ',', header= 0, nrows=50000)
  
  # remove the columns which have no unique elements
  data = data[[col for col in data if data[col].nunique() > 1]]
  
  X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))

  # Assign the target column to a variable
  Y=data[target]

  # Split the datase into training and testing dataset
  X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(X,Y, data.index, test_size=0.2, random_state=0)
  
  #Linear SVC
  lsvc = LinearSVC()
  y_pred_LSVC = lsvc.fit(X_train, y_train).predict(X_test)
  best_model = lsvc.fit(X_train, y_train)
  lsvc_accr = metrics.accuracy_score(y_test,y_pred_LSVC)*100
  best_accr = lsvc_accr
  
  #KNN
  knn = KNeighborsClassifier()
  y_pred_knn = knn.fit(X_train, y_train).predict(X_test)
  knn_accr = metrics.accuracy_score(y_test, y_pred_knn)*100
  
  #DTC
  clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 0)
  clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 0)
  y_pred_DTC_gini = clf_gini.fit(X_train, y_train).predict(X_test)
  y_pred_DTC_entropy = clf_entropy.fit(X_train, y_train).predict(X_test)
  dtc_gini_accr = metrics.accuracy_score(y_test,y_pred_DTC_gini)*100
  dtc_entropy_accr = metrics.accuracy_score(y_test,y_pred_DTC_entropy)*100
  
  #Multinomial NB
  mnb_model=MultinomialNB()
  y_pred_mnb=mnb_model.fit(X_train,y_train).predict(X_test)
  mnb_accr = metrics.accuracy_score(y_test,y_pred_mnb)*100

  #Bernoulli NB
  bnb_model=BernoulliNB()
  y_pred_bnb=bnb_model.fit(X_train,y_train).predict(X_test)
  bnb_accr = metrics.accuracy_score(y_test,y_pred_bnb)*100

  #Gaussian NB

  gnb_model=GaussianNB()
  y_pred_gnb=gnb_model.fit(X_train,y_train).predict(X_test)
  gnb_accr = metrics.accuracy_score(y_test,y_pred_gnb)*100

  #ADB

  adb = AdaBoostClassifier(n_estimators=200, learning_rate=1)
  #Train Adaboost Classifer
  y_pred_ada = adb.fit(X_train, y_train).predict(X_test)
  adb_accr = metrics.accuracy_score(y_test, y_pred_ada)*100
  
  #XGB

  xgb = XGBClassifier()
  y_pred_xgb = xgb.fit(X_train, y_train).predict(X_test)
  xgb_accr = metrics.accuracy_score(y_test, y_pred_xgb)*100
  
  #Random Forest Classifier 

  rfc=RandomForestClassifier(n_estimators=100)
  y_pred_rfc=rfc.fit(X_train,y_train).predict(X_test)
  rfc_accr = metrics.accuracy_score(y_test, y_pred_rfc)*100

  if(best_accr<knn_accr):
    best_accr = knn_accr
    best_model = knn.fit(X_train, y_train)
  elif(best_accr<dtc_gini_accr):
    best_accr = dtc_gini_accr
    best_model = clf_gini.fit(X_train, y_train)
  elif(best_accr<dtc_entropy_accr):
    best_accr = dtc_entropy_accr
    best_model = clf_entropy.fit(X_train, y_train)
  elif(best_accr<mnb_accr):
    best_accr = mnb_accr
    best_model = mnb_model.fit(X_train, y_train)
  elif(best_accr<bnb_accr):
    best_accr = bnb_accr
    best_model = bnb_model.fit(X_train, y_train)
  elif(best_accr<gnb_accr):
    best_accr = gnb_accr
    best_model = gnb_model.fit(X_train, y_train)
  elif(best_accr<adb_accr):
    best_accr = mnb_accr
    best_model = mnb_model.fit(X_train, y_train)
  elif(best_accr<xgb_accr):
    best_accr = xgb_accr
    best_model = xgb_model.fit(X_train, y_train)
  elif(best_accr<rfc_accr):
    best_accr = rfc_accr
    best_model = rfc_model.fit(X_train, y_train)
    
  
  

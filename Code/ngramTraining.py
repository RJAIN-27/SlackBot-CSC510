from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import modelTraining as mt
import commonFunctions as cf

def ngram(data, target, f):
    cols = list(data.columns)
    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2),
                            stop_words='english')
    col_mod_dict = {}
    for col in cols:

        if not(data[col].dtypes=='float64' or data[col].dtypes=='int64') and col!=target:
            try:
                features = tfidf.fit_transform(data[col]).toarray()
                X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, data[target], data.index, test_size=0.2,
                                                                                                 random_state=0)
                f.writelines("\n        Model accuracies when ngram based classification is performed on column " + str(col))
                models = mt.modelTraining(X_train, X_test, y_train, y_test,f)
                f.writelines("\n        Best model when ngram based classification is performed on column " + str(col))
                best = cf.bestModel(models,f)

                col_mod_dict[col]=best
                for model in best:
                    f.writelines("\n            "+model)
                f.writelines("\n")

            except Exception as e:
                print(e)
                f.writelines("\n        Cannot transform  " +str(col ) +" to array.")
    return col_mod_dict

"""
Helper to match a string with instantiating a specific ML algorithm
"""

def handle_classify_algorithm(algorithm):
    algo_name = str(algorithm).lower().strip()
    if algo_name == "svm" or algo_name == "svc":
        from sklearn import svm
        return svm.SVC()
    elif algo_name == "logistic" or algo_name == "logisticregression":
        from sklearn.linear_model import LogisticRegression
        return LogisticRegression()
    elif algo_name == "forest" or algo_name == "randomforestclassifier":
        from sklearn.ensemble import RandomForestClassifier
        return RandomForestClassifier()
    elif algo_name == 'bayes' or algo_name == "multinomialnb":
        from sklearn.naive_bayes import MultinomialNB
        return MultinomialNB()
    elif algo_name == 'knn' or algo_name == "kneighborsclassifier":
        from sklearn.neighbors import KNeighborsClassifier
        return KNeighborsClassifier(n_neighbors=5)
    else:
        return None


def handle_regress_algorithm(algorithm):
    algo_name = str(algorithm).lower().strip()
    if algo_name == "simple" or algo_name == "linearregression":
        from sklearn import linear_model
        return linear_model.LinearRegression(fit_intercept = True)
    elif algo_name == "lasso":
        from sklearn import linear_model
        return linear_model.Lasso(alpha=0.1)
    elif algo_name == "ridge":
        from sklearn import linear_model
        return linear_model.Ridge(alpha=0.1)
    elif algo_name =='elastic' or algo_name =="elasticnet":
        from sklearn.linear_model import ElasticNet
        return ElasticNet(alpha=0.1)

    else:
        return None


def handle_cluster_algorithm(algorithm):
    algo_name = str(algorithm).lower().strip()
    if algo_name == "kmeans":
        from sklearn.cluster import KMeans
        return KMeans()
    else:
        return None


def check_all(algorithm):
    """
    Checks the algorithm parameter with all classification, regression, and clustering algorithms
    (returns the model with the first match in this order)
    """
    cl = handle_classify_algorithm(algorithm)
    reg = handle_regress_algorithm(algorithm)
    clu = handle_cluster_algorithm(algorithm)

    if cl is not None:
        return cl
    elif reg is not None:
        return reg
    elif clu is not None:
        return clu
    else:
        print("No matching algorithm for '" + str(algorithm) + "'")
        return None

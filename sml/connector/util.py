_keywords = {
            'load':['fileName'],
            'read':['fileName', 'header', 'sep', 'dtypes'],
            'split':['train_split','test_split','persist_names_split'],
            'replace':['replaceColumns','replaceValue','replaceIdentifier','replacePersist'],
            'classify': ['predictors', 'label', 'algorithm', 'feature'],
            'regress': ['predictors', 'label', 'algorithm', 'feature'],
            'cluster': ['predictors', 'label', 'numClusters','algorithm', 'feature'],
            'save': ['savefile'],
            'encode':['encodeStrategy', 'encodePersist'],
            'apply':['applyFileName', 'applyHeader', 'applySep', 'applyDTypes','applyPredictors','applyLabel'],
            'plot':['plot_model_type', 'plot_type_values']
             }
_listOptions = ['predictors', 'dtypes','applyDTypes','persist_names_split','applyPredictors']
def keyword_check(parsing):
    '''
    Maps parsed string to dictionary
    :returns dictionary of keywords with values from Query.
    '''

    keys = {}
    for key in _keywords:
        parse_check = None
        try:
            parse_check = parsing[key]
        except KeyError:
            parse_check = ""
        if (parse_check is not None) and (parse_check != ""):
            keys[key] = {}
            for innerKey in _keywords[key]:
                try:
                    if innerKey in _listOptions:
                        keys[key][innerKey] = [x.strip() for x in parsing[innerKey].split(',')]
                    else:
                        keys[key][innerKey] = parsing[innerKey]
                except KeyError:
                    keys[key][innerKey] = None
            if keys[key] == {}:
                keys[key] = True
        else:
            keys[key] = None
    return keys

def get_algo(keywords):
    '''
    :keywords - dictionary
    :returns type of algorithm used.
    '''

    if not keywords.get('classify') and not keywords.get('regress') and not keywords.get("cluster"):
        return "none"
    elif keywords.get("classify") and not keywords.get("regress") and not keywords.get("cluster"):
        return "classify"
    elif not keywords.get("classify") and keywords.get("regress") and not keywords.get("cluster"):
        return "regress"
    elif not keywords.get("classify") and not keywords.get("regress") and keywords.get("cluster"):
        return "cluster"
    else:
        return "multiple"

def split_dataframe(df, preds, label):
    pred_cols = list()
    for pred in preds:
        pred_cols.append(int(pred) - 1)
    print(pred_cols)

    #Convert label from a string to an int
    label_col = int(label) - 1
    print(label_col)
    X = df.ix[:,pred_cols]
    y = df.ix[:,label_col]

    #items to return
    return X, y

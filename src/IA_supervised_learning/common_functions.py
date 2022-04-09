import pickle

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import warnings
warnings.filterwarnings('ignore')

#Converting a text to numbers is always used but cannot be simplified

def preprocess_text(df,str_txt_column, stop):
    '''
    Preprocess les textes issus de df[str_txt_column] pour pouvoir l'analyser derrière.

    Args:
        df : pandas dataframe des tweets (pd.DataFrame)
        str_txt_column : nom de la colonne où est le texte des tweets (str)
        stop = nltk.corpus.stopwords.words("english")
    
    Returns:
        None 
        Modifie df en place

    Remark :
        Require quite a long time, see how to save the results 
    '''
    print("Start preprocessing texts...")

    # Remove all the special characters
    df[str_txt_column] = df[str_txt_column].str.replace('\W', ' ')

    # remove punctuation
    df[str_txt_column] = df[str_txt_column].str.replace('\w\s', ' ')

    # remove digits
    df[str_txt_column] = df[str_txt_column].str.replace('\d+', ' ')

    # remove all single characters
    df[str_txt_column] = df[str_txt_column].str.replace('\s+[a-zA-Z]\s+', ' ')

    # Remove single characters from the start
    df[str_txt_column] = df[str_txt_column].str.replace('\^[a-zA-Z]\s+', ' ')

    # Removing prefixed 'b'
    df[str_txt_column] = df[str_txt_column].str.replace('^b\s+', ' ')

    # Substituting multiple spaces with single space
    df[str_txt_column] = df[str_txt_column].str.replace('\s+', ' ')

    # Converting to Lowercase
    df[str_txt_column] = df[str_txt_column].str.lower()

    # Remove stopwords
    df[str_txt_column] = df[str_txt_column].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

    #lemmatization
    df[str_txt_column] = df[str_txt_column].apply(lambda x: ' '.join(lemmatizer.lemmatize(x) for x in x.split()))





def evaluate(model,X_train, X_test, y_train, y_test):
    '''
    Verify the model is accurate and does not overfit

    Args :
        model : neural network of classification
        X_train : entries used for training  (np.array)
        X_test :  entries not used for training (np.array)
        y_train : labels used for training  (np.array)
        y_test : labels not used for training (np.array)

    Returns :
        None
    
    '''
    y_pred = model.predict(X_test)  # to predict the sentiment
    print("Accuracy of training model : ", model.score(X_train, y_train))
    #print("Confusion matrix : ", confusion_matrix(y_test, y_pred))
    print("Classification report : \n", classification_report(y_test, y_pred))
    print("Accuracy score : ", accuracy_score(y_test, y_pred))





def save_model(classifier, str_file):
    '''
    Saving and loading model as a pickel

    Args:
        classifier : neural network
        str_file : path where we have to save the classifier

    Returns:
        None

    '''
    with open(str_file, 'wb') as picklefile:
        pickle.dump(classifier, picklefile)

    # load (here str-file = "text_classifier")





def load_model(str_file):
    with open(str_file, 'rb') as training_model:
        model = pickle.load(training_model)
    return model





def apply_model(model, X):
    '''
    Apply the neural network model to X to get prediciton labels y_pred

    Args :
        model : classifier IA (random forest typically) 
        X : !vectorized! texts to analyse (np.array)
    Returns :
        y_pred
    
    Remarks:
        To circumvent the obligation about the type X, [X[0]] works
    '''

    y_pred = model.predict(X)
    return y_pred
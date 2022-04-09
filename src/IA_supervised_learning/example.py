from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pickle
import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')



#################
# Import data set
movie_data = load_files(r"txt_sentoken")
X, y = movie_data.data, movie_data.target

print("len(X) = ", len(X))
####################
# Text preprocessing
documents = []


stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))

    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)

    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)

    # Converting to Lowercase
    document = document.lower()

    # Lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)

    documents.append(document)


###########################
# Converting text to numbers
    # Bag of words approach

vectorizer = CountVectorizer(
    max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()


'''
max_features = nbre de mots retenus
min_df = nbre minimal de docs contenant ce mot
max_df = occurence maximal du mots dans les docs (en pourcentage)

Drawback : It assigns a score to a word based on its occurrence in a particular document. 
It doesn't take into account the fact that the word might also be having a high frequency 
of occurrence in other documents as well.
That's why TFIDF is used
'''

# Finding TFIDF (Term Frequency, Inverse Document Frequency)
'''
Term frequency = (Number of Occurrences of a word)/(Total words in the document)
IDF(word) = Log((Total number of documents)/(Number of documents containing the word))
'''

# to convert from bag of words values to TFIDF ones :
tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

#####################
#Training and testing

# Making sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# training
'''
Random Forest Algorithm  (use RandomForestClassifier class from the sklearn.ensemble library)
//the neural network we use here
'''

classifier = RandomForestClassifier(n_estimators=100, random_state=0)

from timeit import timeit


print(timeit(lambda : classifier.fit(X_train, y_train), number=1))
#################
# Evaluating Model

def evaluate(model):
    y_pred = model.predict(X_test)  # to predict the sentiment
    print("Accuracy of training model : ", model.score(X_train, y_train))
    print("Confusion matrix : ", confusion_matrix(y_test, y_pred))
    print("Classification report : ", classification_report(y_test, y_pred))
    print("Accuracy score : ", accuracy_score(y_test, y_pred))

evaluate(classifier)

#####################################
# Saving and loading model as a pickel

# save
def save_model(classifier, str_file):
    with open(str_file, 'wb') as picklefile:
        pickle.dump(classifier, picklefile)

    # load (here str-file = "text_classifier")

save_model(classifier, "text_clasifier_example")

def load_model(str_file):
    with open(str_file, 'rb') as training_model:
        model = pickle.load(training_model)

    # use it


def apply_model(model, X_test):
    y_pred2 = model.predict(X_test)

    print(confusion_matrix(y_test, y_pred2))
    print(classification_report(y_test, y_pred2))
    print(accuracy_score(y_test, y_pred2))

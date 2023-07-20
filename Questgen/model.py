import nltk
nltk.download('stopwords')
from pprint import pprint
import main
def getModel():
    qg = main.QGen()
    return qg
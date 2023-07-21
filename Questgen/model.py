import nltk
nltk.download('stopwords')
nltk.download('universal_tagset')
from pprint import pprint
import main
def getModel():
    qg = main.QGen()
    return qg
import nltk
nltk.download('stopwords')
from pprint import pprint
from Questgen import main
qg = main.QGen()

payload = {
            "input_text": "Sachin Ramesh Tendulkar is a former international cricketer from India and a former captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket. He is the highest run scorer of all time in International cricket."
        }
print(type(payload))
output = qg.predict_mcq(payload)
print(type(output))
pprint(output)
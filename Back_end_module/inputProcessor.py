import re
import string 
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords


def convert_to_lower(text):
    return text.lower()

def remove_numbers(text):
    number_pattern = r'\d+'
    without_number = re.sub(pattern=number_pattern, repl=" ", string=text)
    return without_number

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text):
    removed = []
    stop_words = list(stopwords.words("english"))
    tokens = word_tokenize(text)
    for i in range(len(tokens)):
        if tokens[i] not in stop_words:
            removed.append(tokens[i])
    return " ".join(removed)

def remove_extra_white_spaces(text):
    single_char_pattern = r'\s+[a-zA-Z]\s+'
    without_sc = re.sub(pattern=single_char_pattern, repl=" ", string=text)
    return without_sc

def lemmatizing(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    for i in range(len(tokens)):
        lemma_word = lemmatizer.lemmatize(tokens[i])
        tokens[i] = lemma_word
    return " ".join(tokens)

def preprocessText(text):
    text = convert_to_lower(text)
    text = remove_numbers(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = remove_extra_white_spaces(text)
    text = lemmatizing(text)

    return text

def processInput(job_data):
    new_record = {
        'title': preprocessText(job_data["job_title"]),
        'employment_type': job_data["employment_type"],
        'required_experience': job_data["seniority_level"],
        'text_length': len(preprocessText(job_data["job_description"]))
    }

    return new_record
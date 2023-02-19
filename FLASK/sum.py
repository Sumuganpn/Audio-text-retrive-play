import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PyPDF2 import PdfReader


def print_keyword(a):
# Open the PDF file 
    c = 'uploads/'+ a
    with open(c, 'rb') as file:
        pdf = PdfReader(file)
        # Extract the text from the file
        text = ""
        for page in range(len(pdf.pages)):
            text += pdf.pages[page].extract_text()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    stop_words.update({"es", "ir", "n","what", "there", "upon", "by", "button", "also", "an", "and", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "did", "do", "does", "else", "for", "from", "get", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "i", "if", "in", "into", "is", "it", "its", "like", "more", "me", "my", "no", "nor", "not", "of", "on", "one", "or", "other", "our", "out", "over", "said", "same", "she", "should", "so", "some", "such", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "to", "too", "us", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "you", "your"})

    tokens = [token.lower() for token in tokens if token.lower() not in stop_words]

    # remove empty strings
    tokens = [token for token in tokens if token]

    # remove special symbols
    tokens = [re.sub('[^A-Za-z0-9]+', '', token) for token in tokens]

    # create set to remove duplicate
    tokens = set(tokens)

    # sort the words
    tokens = sorted(tokens)

    # Print the keywords
    return tokens

import streamlit as st
import re
import math
from collections import Counter

def idf(word, documents):
    num_documents_containing_word = sum(1 for document in documents if word in document)
    return math.log(len(documents) / (1 + num_documents_containing_word))

def main():
    st.title("Анализ текстового файла")
    
    uploaded_file = st.file_uploader("Выберите текстовый файл", type=['txt'])
    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode('utf-8')
        text = re.sub(r'[^\w\s]', '', text.lower())
        words = text.split()

        idf_values = {word: idf(word, words) for word in set(words)}

        sorted_words = sorted(idf_values.items(), key=lambda x: x[1], reverse=True)

        top_words = sorted_words[:50]

        st.write("Топ 50 слов:")
        st.write("| Слово | tf | idf |")
        for word, idf_value in top_words:
            tf = words.count(word)
            st.write(f"| {word} | {tf} | {idf_value} |")

if __name__ == "__main__":
    main()
    
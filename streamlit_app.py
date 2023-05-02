import streamlit as st
from langchange.translator import Translator

translator = Translator()

text_input = st.text_input("Enter text to translate")
target_language = st.selectbox("Select target language", ["Spanish", "French", "German"])

translated_text = translator.translate(text_input, target_language)

st.write("Translated text: ", translated_text)

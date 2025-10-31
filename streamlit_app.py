import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
st.set_page_config(page_title="Great translation website")
st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

st.title('Streamlit')

st.header('Wprowadzenie do zajęć')

st.subheader('O Streamlit')

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')

st.code("st.write()", language='python')

with st.echo():
    st.write("Echo")

df = pd.read_csv("DSP_4.csv", sep = ';')
st.dataframe(df)

st.header('Przetwarzanie języka naturalnego')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "???",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)


col1, col2 = st.columns([3,1])
with col1:
    st.header('Tlumacz EN -> DE')
with col2:
    st.image( "https://huggingface.co/front/assets/huggingface_logo-noborder.svg", width=120)

with st.expander("Jak korzystać?"):
    st.markdown(
        """
        1. Wybierz "Tłumaczenie EN -> DE" z listy poniżej
        2. Podaj tekst po angielsku
        3. Kliknij przełtumacz
        4. Otrzymasz wynik po niemiecku
        """
    )

translateOption = st.selectbox(
    "Moduł tłumaczenia",
    ["= wybierz =", "Tłumaczenie EN -> DE"]
)

if translateOption == "Tłumaczenie EN -> DE":
    st.subheader("Tłumaczysz tekst z angielskiego na niemiecki")
    text_eng = st.text_area(label="Podaj tekst")


    run_btn = st.button("Tłumacz")


    if run_btn:
        if not text_eng.strip():
            st.error("Podaj tekst")
        else:
            try:
                with st.spinner('Tłumaczenie...'):
                    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
                    result = translator(text_eng)
                    st.success("Przetłumaczono")
                    st.write(result[0]["translation_text"])

            except Exception as e:
                st.error(f"Coś poszło nie tak:{e}")
st.write("s28904")
import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek
st.set_page_config(page_title="Great translation website")
st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Lab05. Streamlit')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

with st.echo():
    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

df = pd.read_csv("DSP_4.csv", sep = ';')
st.dataframe(df)
# musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

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
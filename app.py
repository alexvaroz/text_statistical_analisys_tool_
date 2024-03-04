import streamlit as st
import re
from collections import Counter
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def tokenizing_regex(text):
  regex = r'\w+'
  return re.findall(regex,text.lower())

def counting_tokens(tokens, top_frequencies=15):
    return Counter(tokens).most_common(top_frequencies)  

def ploting_most_frequent_woords_bar(words_tuple):
    number_words = len(words_tuple)
    words, freq = zip(*words_tuple)
    fig=go.Figure(go.Bar(x=list(words),
                     y=list(freq), text=list(freq), textposition='outside'))
    fig.update_layout( autosize=False,
        width=800,
    height=500,
    title_text='Top {} Frequent Words'.format(number_words))
    fig.update_xaxes(tickangle = -45)
    return fig


st.title("Text's Statistical Analyzer Tool")

text_input = st.text_area("Text input")


if text_input != '':
   word_tuples = counting_tokens(tokenizing_regex(text_input))
   st.plotly_chart(ploting_most_frequent_woords_bar(word_tuples), use_container_width=True)
   st.text(word_tuples)
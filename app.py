import streamlit as st
import re
from collections import Counter
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import nltk
nltk.download('stopwords')


def tokenizing_regex(text):
  regex = r'\w+'
  return re.findall(regex,text.lower())


def stopwords_removal(tokens, language='english'):
   stopwords = nltk.corpus.stopwords.words(language)
   tokens_limpos=[]
   for item in tokens:
    if (item not in stopwords) & (len(item) > 2) :
       tokens_limpos.append(item)
   return tokens_limpos


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

def word_cloud_generator(tokens):
   str_tokens = " ".join(s for s in tokens)
   wordcloud = wordcloud = WordCloud(background_color="#f5f5f5").generate(str_tokens)
   return wordcloud



st.title("Text's Statistical Analyzer Tool")

def submit():
   st.text(text_input)
   tokens = tokenizing_regex(text_input)
   tokens = stopwords_removal(tokens, "portuguese")
   word_tuples = counting_tokens(tokens)
   st.plotly_chart(ploting_most_frequent_woords_bar(word_tuples), use_container_width=True)
   fig = plt.figure(figsize=(10, 12))
   plt.imshow(word_cloud_generator(tokens), interpolation="bilinear")
   plt.axis("off")
   plt.tight_layout(pad=0)
   st.pyplot(fig)

   
def clear_text_area():
    st.session_state.text_input = st.session_state.widget
    st.session_state.widget = ''

text_input = st.text_area("Text to analyse", key="widget", on_change=submit)

#if 'text_input' not in st.session_state:
#    st.session_state.text_input = ''


   


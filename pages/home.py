import streamlit as st
from pages.fetch import*


def main():
	front_up()

	st.markdown("""
			
			 This is a Natural Language Processing(NLP) Based App useful for basic NLP task
			implemented using State of he Art API's on Streamlit Framework
			""")
	### features

	st.header('Features')

	st.markdown("""
			#### Basic NLP Tasks:
			+ App covers the most basic NLP task of tokenisation, parts of speech tagging.
				You can paste the desired content or may directly pass the url for the text.
			#### Named Entity Recognition and Topic Modelling:
			+ Named Entites like organistion person etc are recognised and top topics from the corpus
				are found based on LDA modelling.
			#### Machine Translations:
			+ Machine Translation, or aka Language Translation. App uses Googel TRanslate API.Currently 
				app has options for 10-15 languages.
			
			#### Text Summarisation:
			+ It summerizes the given text into few lines. One can copy paste the article or may direclty
				pass the URL.It has options to use Gensim, Sumy.
			""")

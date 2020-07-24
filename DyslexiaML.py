"""Main module for the streamlit NLPJenny app"""
import streamlit as st


import pages.home
import pages.basicNLP
#import pages.captionGenerator
import pages.nertm
import pages.machineTranlation
import pages.textSummarization


PAGES = {
    "Home": pages.home,
    "Basic NLP": pages.basicNLP,
    "NER and Topic Modelling": pages.nertm,
    "Text Summarization": pages.textSummarization,
    "Machine Translation": pages.machineTranlation
    #"Caption Generator": pages.captionGenerator
}


def main():

    st.sidebar.title("NLPJenny")
    st.sidebar.text("Natural Language Processing On the Go")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGES.keys()))

    #PAGES[page].main()

    with st.spinner(f"Loading {page} ..."):
        PAGES[page].main()

    st.sidebar.title("About App")

    st.sidebar.info(
        """
        This App uses State of the Art free tier API's from different paltforms
        like IBM,Google Cloud and libraries like Spacy,Genism, NLTK and Textblob etc. 
        It uses Streamlit for implemention of beatiful and easy web app.
        """
    )

    st.sidebar.title("Contact Developer")
    st.sidebar.info(
        """
        This app is develop by Aryan. You can contact me at
        [aryan chaudhary](https://aryanc55.github.io).
"""
    )

   #st.sidebar.markdown("[![Github](https://github.com/aryanc55/NLPJenny/blob/master/assests/github.png?raw=true)](https://github/aryanc55)")

    st.sidebar.markdown(
        """  [Github](https://github.com/aryanc55)""")  # change all thses three to  to iamge
    st.sidebar.markdown("""  [Twitter](https://twitter.com/aryanc55)""")
    st.sidebar.markdown("""  [Medium](https://medium.com/@aryanc55)""")

    st.sidebar.title("Souce Code")
    st.sidebar.info(
        "This an free to use template repository and you are very welcome to **contribute** your awesome "
        "comments, questions, resources and apps as "
        "[issues](https://github.com/aryanc55/NLPJenny/issues) of or "
        "[pull requests](https://github.com/aryanc55/NLPJenny/pulls) "
        "to the [source code](https://github.com/aryanc55/NLPJenny). "
    )


if __name__ == "__main__":
    main()

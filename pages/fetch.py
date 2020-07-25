import streamlit as st
import pandas as pd
#from pages.login import result
#from pages.login import PRIMARY_KEY


def front_up():
    html_temp = """
		<div style="background-color:#ff1a75;padding:10px">
		<h1 style="color:white;text-align:center;">DyslexiaML</h1>
		<h4 style="color:white;text-align:center;">"AI for Dyslexia"</h4>
		</div>
		<br></br>
		<br></br>
	"""
    st.markdown(html_temp,unsafe_allow_html=True)
    





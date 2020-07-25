import streamlit as st

#from pages.login import result
#from pages.login import PRIMARY_KEY

from bs4 import BeautifulSoup
from urllib.request import urlopen
# Fetch Text From Url

def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return fetched_text

def selection(key):
	option = st.selectbox('How would you like to provide the data?',('URL', 'Paste/Write Text'), index=1, key=key)
	st.write('You selected:', option)
	if option == 'Paste/Write Text' :
		message = st.text_area("Enter Text", "Type Here ..", key=key+'text')
		return (0,message)
	else:
		url = st.text_area("Enter URL", "Paste Here ..", key= key+'url')
		return (1,url)

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
    


def front_down():
    #closing remarks
    pass

def result():
    pass

def contact():
    pass    
	#st.markdown(html,unsafe_allow_html=True)

# def submit(ans =None, question =None):
#     marks= 0
#     if question =="1":
#         if ans =='Yes':
#             marks = 4
#         else:
#             marks = 0
            
    
#     elif question =="2":
#         if ans == 'Grapes':
#             marks = 4
#         else:
#             marks=0
               
#     if question =="3":
#         if ans =='No':
#             marks=4
#         else:
#             marks =0
    
#     elif question =="4":
#         if ans == "The First Letter":
#             marks =4
#         else:
#             marks =0
    
#     if question =="5":
#         if ans =="C":
#             marks=4
#         else:
#             marks=0
    
#     elif question =="6":
#         if ans == "b":
#             marks = 4
#         else:
#             marks=0
    
    
#     if question =="7":
#         if ans =="ED":
#             marks=4
#         else:
#             marks=0
    
#     elif question =="8":
#         if ans =="Dog":
#             marks=4
#         else:
#             marks=0
    
    
    
#     if question =="9":
#         if ans == "First one is left and next one is right":
#             marks=4
#         else:
#             marks=0
			
    
#     elif question =="10":
#         if ans == "cake":
#             marks=4
#         else:
#             marks=0
    
#     return marks

def database(page =None,PRIMARY_KEY=None,marks={}):
    st.write(marks)

def sdatabase(page =None):
    pass
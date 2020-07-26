import streamlit as st
from pages.fetch import*


def main():
	front_up()
 
	st.image(image = "https://github.com/dyslexiaworkin/DyslexiaML/blob/master/dyslexia.jpg?raw=true",width =700)

	st.markdown("""
			
			 <h4 align="center" id="a"><i>"Children are a nation’s most valuable assets!"</i></h4>

			""", unsafe_allow_html=True)
	### features
 
	st.markdown(""" 

  A learning disability is a problem that affects how a person receives and processes information. People with learning disabilities may have trouble with any of the following:


+ Reading
+ Writing
+ Doing math
+ Understanding directions
+ Learning disabilities are common. 



Learning disabilities have nothing to do with how smart a person is. Rather, a person with a learning disability may just see, hear, or understand things differently. 
That can make everyday tasks, such as studying for a test or staying focused in class, much more difficult. There are strategies a person can learn to make it easier 
to cope with these differences.

Types of Learning Disabilities
There are many different kinds of learning disabilities, and they can affect people differently. It's important to note that attention deficit hyperactivity disorder (ADHD)
and autism spectrum disorders are not the same as learning disabilities.</br>

""", unsafe_allow_html=True)

	st.header('More about Dyslexia')
	st.subheader("This is what reading with dyslexia may look like!")
	st.image(image ='https://github.com/dyslexiaworkin/DyslexiaML/blob/master/dyslexia-zoomedout.gif?raw=true', width =700)
 	

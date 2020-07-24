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
	
Learning disabilities have nothing to do with how smart a person is. Rather, a person with a learning disability may just see, hear, or understand things differently. 
That can make everyday tasks, such as studying for a test or staying focused in class, much more difficult. There are strategies a person can learn to make it easier 
to cope with these differences.

There are many different kinds of learning disabilities, and they can affect people differently. It's important to note that attention deficit hyperactivity disorder (ADHD)
and autism spectrum disorders are not the same as learning disabilities.</br>

Dyslexia is a learning disability in reading. People with dyslexia have trouble reading at a good pace and without mistakes. They may also have a hard time with reading comprehension, spelling, and writing. But these challenges aren’t a problem with intelligence.

Dyslexia can create difficulty with other skills, too. These include:

 -> Reading comprehension

 -> Spelling

 -> Writing

 -> Math  

Dyslexia Signs and Symptoms

Dyslexia impacts people in different ways. So, symptoms might not look the same from one person to another.A key sign of dyslexia is trouble decoding words. This is the ability to match letters to sounds. Kids can also struggle with a more basic skill called phonemic awareness. This is the ability to recognize the sounds in words. Trouble with phonemic awareness can show up as early as preschool.


Possible Causes of Dyslexia

Researchers haven’t yet pinpointed exactly what causes dyslexia. But they do know that genes and brain differences play a role. Here are some of the possible causes of dyslexia:
Genes and heredity: Dyslexia often runs in families. About 40 percent of siblings of people with dyslexia also struggle with reading. As many as 49 percent of parents of kids with dyslexia have it, too. Scientists have also found genes linked to problems with reading and processing language.
Brain anatomy and activity: Brain imaging studies have shown brain differences between people with and without dyslexia. These differences happen in areas of the brain involved with key reading skills. Those skills are knowing how sounds are represented in words, and recognizing what written words look like.
""", unsafe_allow_html=True)

	st.header('More about Dyslexia')
	st.subheader("This is what reading with dyslexia may look like!")
	st.image(image ='https://github.com/dyslexiaworkin/DyslexiaML/blob/master/dyslexia-zoomedout.gif?raw=true', width =700)
 	

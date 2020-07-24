import streamlit as st
from pages.fetch import*

def main():
    front_up()
    st.title("QUIZ")
    
    if st.checkbox('Question I', key ='q1'):
        st.info("Check whether these two alphabets  are same or not?")
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/O.png?raw=true',width=100)
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/o.png?raw=true', width=100)
        
        ansq1 = st.radio("Answer:", ['Yes','No'], key ='q1')
        
        if st.button("SUBMIT", key='q1'):
            st.write(ansq1)
            submit(ans = ansq1, question ="1")
            
            
    
    if st.checkbox('Question II', key ='q2'):
        st.info("Guess the fruit in the picture. ")
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/grapes.jpg?raw=true',width=100)
        
        ansq2 = st.radio("Answer:", ['Orange','Banana','Grapes','Mango'], key ='q2')
        
        if st.button("SUBMIT", key='q2'):
            st.write(ansq2)
            submit(ans = ansq2, question ="2")
            
            
            
    
    if st.checkbox('Question III', key ='q3'):
        st.info("Check whether these two alphabets  are same or not?")
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/p.png?raw=true',width=100)
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/q.png?raw=true',width=100)
        
        
        ansq3 = st.radio("Answer:", ['Orange','Banana','Grapes','Mango'], key = 'q3')
        
        if st.button("SUBMIT", key='q3'):
            st.write(ansq3)
            submit(ans = ansq3, question ="3")
            
            
            
    
    if st.checkbox('Question IV', key ='q4'):
        st.info("Which letter is G?")
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/G.jpg?raw=true',width=100)
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/C.png?raw=true',width=100)
        
        
        ansq4 = st.radio("Answer,from left to right:", ['The First Letter','The Second Letter'], key = 'q4')
        
        if st.button("SUBMIT", key='q4'):
            st.write(ansq1)
            submit(ans = ansq4, question ="4")
            
    
    if st.checkbox('Question V', key ='q5'):
        st.info("Which letter CAT starts with?")
        # st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/G.jpg?raw=true',width=100)
        # st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/C.png?raw=true',width=100)
        
        
        ansq5 = st.radio("Answer:", ['F','C','A','T'], key = 'q5')
        
        if st.button("SUBMIT", key='q5'):
            st.write(ansq5)
            submit(ans = ansq5, question ="5")
            
    
    if st.checkbox('Question VI', key ='q6'):
        st.info("What is the smaller version of this letter?")
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/B.png?raw=true',width=100)
        # st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/C.png?raw=true',width=100)
        
        
        ansq6 = st.radio("Answer:", ['d','b'], key = 'q6')
        
        if st.button("SUBMIT", key='q6'):
            st.write(ansq6)
            submit(ans = ansq6, question ="6")
    
    
    if st.checkbox('Question VII', key ='q7'):
        st.info("What do you hear?")
        st.audio(data = 'https://github.com/dyslexiaworkin/artgallery/blob/master/ed.mpeg?raw=true')	
        
        ansq7 = st.radio("Answer:", ['AB','ED'], key = 'q7')
        
        if st.button("SUBMIT", key='q7'):
            st.write(ansq7)
            submit(ans = ansq7, question ="7")
    
    
    if st.checkbox('Question VIII', key ='q8'):
        st.info("What do you see in the picture?")
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/Dog.jpg?raw=true',width=100)
        
        ansq8 = st.radio("Answer:", ['Cat','Dog'], key = 'q8')
        
        if st.button("SUBMIT", key='q8'):
            st.write(ansq8)
            submit(ans = ansq8, question ="8")
    
    
    if st.checkbox('Question IX', key ='q9'):
        st.info("Which hand is left and Which hand is right?")
        st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/hands.jpg?raw=true',width=100)
        
        ansq9 = st.radio("Answer:", ['First one is right and next one is left','First one is left and next one is right'], key = 'q9')
        
        if st.button("SUBMIT", key='q9'):
            st.write(ansq9)
            submit(ans = ansq9, question ="9")
    
    
    if st.checkbox('Question X', key ='q10'):
        st.info("What do you hear?")
        st.audio(data = 'https://github.com/dyslexiaworkin/artgallery/blob/master/cake.mpeg?raw=true')	
        
        ansq10 = st.radio("Answer:", ['c','l','t','f'], key = 'q10')
        
        if st.button("SUBMIT", key='q10'):
            st.write(ansq10)
            submit(ans = ansq10, question ="10")
    
    
    
    if st.button("Submit the quiz", key='submit'):
        if bool(ansq1) and bool(ansq2) and bool(ansq3) and bool(ansq4) and bool(ansq5) and if bool(ansq6) and bool(ansq7) and bool(ansq8) and bool(ansq9) and and bool(ansq10)  
        database(page = 'quiz') #push ot database
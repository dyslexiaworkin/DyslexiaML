import streamlit as st
from pages.fetch import*
from pages.login import login_dict
from pages.login import name_dict
import MySQLdb



def main():
    front_up()
    try:
        st.write('User Logged in as',name_dict['name'])
        pk = login_dict["key"]
        na = name_dict['name']
        st.write("primary key" ,pk)
        st.write("nane " ,na)
    except:
        st.error(" Please Log in")
    
    st.title("SURVEY")
    try:
        st.write('User Logged in as',name_dict['name'])
    except:
        st.error(" Please Log in to use this feature")
    #st.write(login_dict)
    if st.checkbox('Question I', key ='q1'):
        st.info(" Did your child struggle to learn to count?")
        
        ansq1 = st.radio("Answer:", ['Yes','No'], key ='q1')
        
        if st.button("SUBMIT", key='q1'):
            st.write(ansq1)
            submit(ans = ansq1, question ="1")
            
            
    
    if st.checkbox('Question II', key ='q2'):
        st.info("Does he/she say numbers out of order — long after peers have mastered this skill? ")
        
        ansq2 = st.radio("Answer:",  ['Yes-frequently','Sometimes','No-never'], key ='q2')
        
        if st.button("SUBMIT", key='q2'):
            st.write(ansq2)
            submit(ans = ansq2, question ="2")
            
            
            
    
    if st.checkbox('Question III', key ='q3'):
        st.info(" Does your child not seem to understand the connection between the symbol “4” and the word “four?” Does he make mistakes when reading or following directions involving number words and symbols?")
        
        ansq3 = st.radio("Answer:",  ['Yes-frequently','Sometimes','No -never'], key = 'q3')
        
        if st.button("SUBMIT", key='q3'):
            st.write(ansq1)
            submit(ans = ansq3, question ="3")
            
            
            
    
    if st.checkbox('Question IV', key ='q4'):
        st.info("Does your child struggle to connect the concept of numbers to real-world items? When you ask him how many cookies are left, for example, does he seem confused by the question or answer incorrectly?")
        
        
        ansq4 = st.radio("Answer",['Yes-frequently','Sometimes','No-never'], key = 'q4')
        
        if st.button("SUBMIT", key='q4'):
            st.write(ansq4)
            submit(ans = ansq4, question ="4")
            
    
    if st.checkbox('Question V', key ='q5'):
        st.info("Does your child not seem to understand the difference between adding and subtracting? Does she confuse the  +  and  –  symbols when completing math problems?")
        
        ansq5 = st.radio("Answer:", ['Yes-frequently','Sometimes','No-never'], key = 'q5')
        
        if st.button("SUBMIT", key='q5'):
            st.write(ansq5)
            submit(ans = ansq5, question ="5")
            
    
    if st.checkbox('Question VI', key ='q6'):
        st.info("Does your child still count on his fingers past third grade?")
    
        ansq6 = st.radio("Answer:",['Yes-frequently','Sometimes','No-never'], key = 'q6')
        
        if st.button("SUBMIT", key='q6'):
            st.write(ansq6)
            submit(ans = ansq6, question ="6")
    
    
    if st.checkbox('Question VII', key ='q7'):
        st.info(" Difficulty sustaining attention; seems ""hyper"" or ""daydreamer"" ")
        
        ansq7 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q7')
        
        if st.button("SUBMIT", key='q7'):
            st.write(ansq7)
            submit(ans = ansq6, question ="7")
    
    
    if st.checkbox('Question VIII', key ='q8'):
        st.info("Confused by letters, numbers, words, sequences, or verbal explanations.")
        
        ansq8 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q8')
        
        if st.button("SUBMIT", key='q8'):
            st.write(ansq8)
            submit(ans = ansq8, question ="8")
    
    
    if st.checkbox('Question IX', key ='q9'):
        st.info(" Reads and rereads with little comprehension")
        
        ansq9 = st.radio("Answer:",['Yes','No','Unknown'], key = 'q9')
        
        if st.button("SUBMIT", key='q9'):
            st.write(ansq9)
            submit(ans = ansq9, question ="9")
    
    
    if st.checkbox('Question X', key ='q10'):
        st.info("Difficulty putting thoughts into words; speaks in halting phrases; leaves sentences incomplete.")

        
        ansq10 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q10')
        
        if st.button("SUBMIT", key='q10'):
            st.write(ansq10)
            submit(ans = ansq10, question ="10")
    
    
    
    
    
    if st.checkbox('Question XI', key ='q11'):
        st.info("Can count, but has difficulty counting objects and dealing with money.")

        
        ansq11 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q11')
        
        if st.button("SUBMIT", key='q11'):
            st.write(ansq11)
            submit(ans = ansq11, question ="11")
    
    
    
    
    if st.checkbox('Question XII', key ='q12'):
        st.info("ory for sequences, facts and information that has not been experienced.")

        
        ansq12 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q12')
        
        if st.button("SUBMIT", key='q12'):
            st.write(ansq12)
            submit(ans = ansq12, question ="12")
    
    
    
    if st.checkbox('Question XIV', key ='q13'):
        st.info("Complains of dizziness, headaches or stomach aches while reading.")

        
        ansq13 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q13')
        
        if st.button("SUBMIT", key='q13'):
            st.write(ansq13)
            ssubmit(ans = ansq13, question ="13")
    
    
    
    if st.checkbox('Question XIV', key ='q14'):
        st.info("Is reading extremely difficult? (Below grade or age level.")

        
        ansq14 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q14')
        
        if st.button("SUBMIT", key='q14'):
            st.write(ansq14)
            ssubmit(ans = ansq14, question ="14")
    
    
    
    
    
    
    
    if st.checkbox('Question XV', key ='q15'):
        st.info("Is spelling ability poor? Letters missed, reversed etc?")

        
        ansq15 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q15')
        
        if st.button("SUBMIT", key='q15'):
            st.write(ansq15)
            ssubmit(ans = ansq15, question ="15")
    


    
    if st.checkbox('Question XVI', key ='q16'):
        st.info("Is it difficult to rhyme words?(Not sure? Play a rhyming game with your child or student).")

        
        ansq16 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q16')
        
        if st.button("SUBMIT", key='q16'):
            st.write(ansq16)
            ssubmit(ans = ansq16, question ="16")
    

    
    
    if st.checkbox('Question XVII', key ='q17'):
        st.info("Is there difficulty telling time on a clock with hands and/or tying shoes with laces?")

        
        ansq17 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q17')
        
        if st.button("SUBMIT", key='q17'):
            st.write(ansq17)
            ssubmit(ans = ansq17, question ="17")
    

 
 
    if st.checkbox('Question XVIII', key ='q18'):
        st.info("Is there difficulty finding the right words while speaking? Lots of ums, ahs, 'those things', and 'that stuff'.")

        
        ansq18 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q18')
        
        if st.button("SUBMIT", key='q18'):
            st.write(ansq18)
            ssubmit(ans = ansq18, question ="18")
    


    if st.checkbox('Question XIX', key ='q19'):
        st.info(" Pauses, repeats or makes frequent mistakes when reading aloud.")

        
        ansq19 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q19')
        
        if st.button("SUBMIT", key='q19'):
            st.write(ansq19)
            ssubmit(ans = ansq19, question ="19")
    


    if st.checkbox('Question XX', key ='q20'):
        st.info("Unusually high or low tolerance for pain.")

        
        ansq20 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q20')
        
        if st.button("SUBMIT", key='q20'):
            st.write(ansq20)
            ssubmit(ans = ansq20, question ="20")
    
     
    if st.button("Submit the quiz", key='submit'):
        try:
            if bool(ansq1) and bool(ansq2) and bool(ansq3) and bool(ansq4) and bool(ansq5) and bool(ansq6) and bool(ansq7) and bool(ansq8) and bool(ansq9) and bool(ansq10) and bool(ansq11) and bool(ansq12) and bool(ansq13) and bool(ansq14) and bool(ansq15) and bool(ansq16) and bool(ansq17) and bool(ansq18) and bool(ansq19) and bool(ansq20):
                sdatabase(page = 'quiz') #push ot database
        except:
            st.warning("Please answer all questions")    
        
        
    
    if st.button("Check your result", key='result'):
        #check for each question is answered
        result()
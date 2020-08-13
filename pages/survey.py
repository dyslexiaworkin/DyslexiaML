import streamlit as st
from pages.fetch import*
from pages.login import login_dict
from pages.login import name_dict
from model import prediction
import MySQLdb


def submit(ans =None, question =None):
    marks= 0

    if question == "1" or question == "2" or question == "3"or question == "4"or question == "5"or question == "6":
            if ans == 'No-never':
                marks = 4
            elif ans == 'Sometimes':
                marks = 2
            else:
                marks = 0
        
    else:
        if ans == 'No':
            marks = 4
        elif ans == 'Unknown':
            marks = 2
        else:
            marks = 0
    
    return marks
    
    





diss = {}

def main():
    anssdic={}
    
    front_up()
    try:
        st.write('User Logged in as',name_dict['name'])
        pk = login_dict["key"]
        na = name_dict['name']
        #st.write("primary key" ,pk)
        st.write("Name " ,na)
    except:
        st.error(" Please Log in")
    
    st.title("SURVEY")
    
    
    if st.checkbox('Question I', key ='q1'):
        st.info(" Did your child struggle to learn to count?")
        
        ansq1 = st.radio("Answer:", ['Yes-frequently','Sometimes','No-never'], key ='q1')
        anssdic['ansq1'] =ansq1
        if st.button("SUBMIT", key='q1'):
            st.write(ansq1)
            marks1 = submit(ans = ansq1, question ="1")
            st.write(marks1)
            diss.update({'marks1':marks1})
            #st.write(anssdic)
            #st.write(diss)
            
            
    
    if st.checkbox('Question II', key ='q2'):
        st.info("Does he/she say numbers out of order — long after peers have mastered this skill? ")
        
        ansq2 = st.radio("Answer:",  ['Yes-frequently','Sometimes','No-never'], key ='q2')
        anssdic['ansq2'] = ansq2
        if st.button("SUBMIT", key='q2'):
            st.write(ansq2)
            marks2 = submit(ans = ansq2, question ="2")
            diss.update({'marks2':marks2})
            #st.write(anssdic)
            #st.write(diss)
            
            
            
    
    if st.checkbox('Question III', key ='q3'):
        st.info(" Does your child not seem to understand the connection between the symbol “4” and the word “four?” Does he make mistakes when reading or following directions involving number words and symbols?")
        
        ansq3 = st.radio("Answer:",  ['Yes-frequently','Sometimes','No -never'], key = 'q3')
        anssdic['ansq3'] =ansq3
        if st.button("SUBMIT", key='q3'):
            st.write(ansq3)
            marks3 = submit(ans = ansq3, question ="3")
            diss.update({'marks3':marks3})
            #st.write(anssdic)
            #st.write(diss)
            
            
    
    if st.checkbox('Question IV', key ='q4'):
        st.info("Does your child struggle to connect the concept of numbers to real-world items? When you ask him how many cookies are left, for example, does he seem confused by the question or answer incorrectly?")
        
        
        ansq4 = st.radio("Answer",['Yes-frequently','Sometimes','No-never'], key = 'q4')
        anssdic['ansq4'] = ansq4
        if st.button("SUBMIT", key='q4'):
            st.write(ansq4)
            marks4 = submit(ans = ansq4, question ="4")
            
            diss.update({'marks4':marks4})
            #st.write(anssdic)
            #st.write(diss)
            
    
    if st.checkbox('Question V', key ='q5'):
        st.info("Does your child not seem to understand the difference between adding and subtracting? Does she confuse the  +  and  –  symbols when completing math problems?")
        
        ansq5 = st.radio("Answer:", ['Yes-frequently','Sometimes','No-never'], key = 'q5')
        anssdic['ansq5'] = ansq5
        if st.button("SUBMIT", key='q5'):
            st.write(ansq5)
            marks5 = submit(ans = ansq5, question ="5")
            diss.update({'marks5':marks5})
            #st.write(anssdic)
            #st.write(diss)
            
    
    if st.checkbox('Question VI', key ='q6'):
        st.info("Does your child still count on his fingers past third grade?")
    
        ansq6 = st.radio("Answer:",['Yes-frequently','Sometimes','No-never'], key = 'q6')
        anssdic['ansq6'] = ansq6
        if st.button("SUBMIT", key='q6'):
            st.write(ansq6)
            marks6 = submit(ans = ansq6, question ="6")
            diss.update({'marks6':marks6})
            #st.write(anssdic)
            #st.write(diss)
    
    
    if st.checkbox('Question VII', key ='q7'):
        st.info(" Difficulty sustaining attention; seems ""hyper"" or ""daydreamer"" ")
        
        ansq7 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q7')
        anssdic['ansq7'] = ansq7
        if st.button("SUBMIT", key='q7'):
            st.write(ansq7)
            marks7 = submit(ans = ansq7, question ="7")
            diss.update({'marks7':marks7})
            #st.write(anssdic)
            #st.write(diss)
    
    if st.checkbox('Question VIII', key ='q8'):
        st.info("Confused by letters, numbers, words, sequences, or verbal explanations.")
        
        ansq8 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q8')
        anssdic['ansq8'] =ansq8
        if st.button("SUBMIT", key='q8'):
            st.write(ansq8)
            marks8 = submit(ans = ansq8, question ="8")
            diss.update({'marks8':marks8})
            #st.write(anssdic)
            #st.write(diss)
    
    if st.checkbox('Question IX', key ='q9'):
        st.info(" Reads and rereads with little comprehension")
        
        ansq9 = st.radio("Answer:",['Yes','No','Unknown'], key = 'q9')
        anssdic['ansq9'] = ansq9
        if st.button("SUBMIT", key='q9'):
            st.write(ansq9)
            marks9 = submit(ans = ansq9, question ="9")
            diss.update({'marks9':marks9})
            #st.write(anssdic)
            #st.write(diss)
    
    if st.checkbox('Question X', key ='q10'):
        st.info("Difficulty putting thoughts into words; speaks in halting phrases; leaves sentences incomplete.")

        
        ansq10 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q10')
        anssdic['ansq10'] = ansq10
        if st.button("SUBMIT", key='q10'):
            st.write(ansq10)
            marks10 = submit(ans = ansq10, question ="10")
            diss.update({'marks10':marks10})
            #st.write(anssdic)
            #st.write(diss)
    
    
    
    
    if st.checkbox('Question XI', key ='q11'):
        st.info("Can count, but has difficulty counting objects and dealing with money.")

        
        ansq11 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q11')
        anssdic['ansq11'] = ansq11
        if st.button("SUBMIT", key='q11'):
            st.write(ansq11)
            marks11 = submit(ans = ansq11, question ="11")
            diss.update({'marks11':marks11})
            #st.write(anssdic)
            #st.write(diss)
    
    
    
    if st.checkbox('Question XII', key ='q12'):
        st.info("ory for sequences, facts and information that has not been experienced.")

        
        ansq12 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q12')
        anssdic['ansq12'] = ansq12
        if st.button("SUBMIT", key='q12'):
            st.write(ansq12)
            marks12 = submit(ans = ansq12, question ="12")
            diss.update({'marks12':marks12})
            #st.write(anssdic)
            #st.write(diss)
    
    
    if st.checkbox('Question XIV', key ='q13'):
        st.info("Complains of dizziness, headaches or stomach aches while reading.")

        
        ansq13 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q13')
        anssdic['ansq13']= ansq13
        if st.button("SUBMIT", key='q13'):
            st.write(ansq13)
            marks13 = submit(ans = ansq13, question ="13")
            diss.update({'marks13':marks13})
            #st.write(anssdic)
            #st.write(diss)
    
    
    if st.checkbox('Question XIV', key ='q14'):
        st.info("Is reading extremely difficult? (Below grade or age level.")

        
        ansq14 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q14')
        anssdic['ansq14']= ansq14
        if st.button("SUBMIT", key='q14'):
            st.write(ansq14)
            marks14 = submit(ans = ansq14, question ="14")
            diss.update({'marks14':marks14})
            #st.write(anssdic)
            #st.write(diss)
    
    
    
    
    
    
    if st.checkbox('Question XV', key ='q15'):
        st.info("Is spelling ability poor? Letters missed, reversed etc?")

        
        ansq15 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q15')
        anssdic['ansq15'] =ansq15
        if st.button("SUBMIT", key='q15'):
            st.write(ansq15)
            marks15 = submit(ans = ansq15, question ="15")
            diss.update({'marks15':marks15})
            #st.write(anssdic)
            #st.write(diss)


    
    if st.checkbox('Question XVI', key ='q16'):
        st.info("Is it difficult to rhyme words?(Not sure? Play a rhyming game with your child or student).")

        
        ansq16 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q16')
        anssdic['ansq16'] = ansq16
        if st.button("SUBMIT", key='q16'):
            st.write(ansq16)
            marks16 = submit(ans = ansq16, question ="16")
            diss.update({'marks16':marks16})
            #st.write(anssdic)
            #st.write(diss)

    
    
    if st.checkbox('Question XVII', key ='q17'):
        st.info("Is there difficulty telling time on a clock with hands and/or tying shoes with laces?")

        
        ansq17 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q17')
        anssdic['ansq17'] = ansq17
        if st.button("SUBMIT", key='q17'):
            st.write(ansq17)
            marks17 = submit(ans = ansq17, question ="17")
            diss.update({'marks17':marks17})
            #st.write(anssdic)
            #st.write(diss)

 
 
    if st.checkbox('Question XVIII', key ='q18'):
        st.info("Is there difficulty finding the right words while speaking? Lots of ums, ahs, 'those things', and 'that stuff'.")

        
        ansq18 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q18')
        anssdic['ansq18'] =ansq18
        if st.button("SUBMIT", key='q18'):
            st.write(ansq18)
            marks18 = submit(ans = ansq18, question ="18")
            diss.update({'marks18':marks18})
            #st.write(anssdic)
            #st.write(diss)


    if st.checkbox('Question XIX', key ='q19'):
        st.info(" Pauses, repeats or makes frequent mistakes when reading aloud.")

        
        ansq19 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q19')
        anssdic['ansq19'] =ansq19
        if st.button("SUBMIT", key='q19'):
            st.write(ansq19)
            marks19 = submit(ans = ansq19, question ="19")
            diss.update({'marks19':marks19})
            #st.write(anssdic)
            #st.write(diss)


    if st.checkbox('Question XX', key ='q20'):
        st.info("Unusually high or low tolerance for pain.")

        
        ansq20 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q20')
        anssdic['ansq20'] =ansq20
        if st.button("SUBMIT", key='q20'):
            st.write(ansq20)
            marks20 = submit(ans = ansq20, question ="20")
            diss.update({'marks20':marks20})
            st.write("Your answers",anssdic)
            #st.write(diss)
     
    if st.button("Submit the quiz", key='submit'):
        try:
            if bool(anssdic['ansq1']) and bool(anssdic['ansq2']) and bool(anssdic['ansq3']) and bool(anssdic['ansq4']) and bool(anssdic['ansq5']) and bool(anssdic['ansq6']) and bool(anssdic['ansq7']) and bool(anssdic['ansq8']) and bool(anssdic['ansq9']) and bool(anssdic['ansq10']) and bool(anssdic['ansq11']) and bool(anssdic['ansq12']) and bool(anssdic['ansq13']) and bool(anssdic['ansq14']) and bool(anssdic['ansq15']) and bool(anssdic['ansq16']) and bool(anssdic['ansq17']) and bool(anssdic['ansq18']) and bool(anssdic['ansq19']) and bool(anssdic['ansq20']) :
                conn = MySQLdb.connect("localhost","ryan","mark50","dyslexia" )
                c = conn.cursor()
                query = 'INSERT INTO survey(pk,name,mone,mtwo,mthree,mfour,mfive,msix,mseven,meight,mnine,mten,meleven,mtwelve,mthirteen, mfourteen,mfifteen,msixteen, mseventeen, meighteen,mnineteen,mtwenty) VALUES ("%s", "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (pk,na,diss['marks1'],diss['marks2'],diss['marks3'],diss['marks4'],diss['marks5'],diss['marks6'],diss['marks7'],diss['marks8'],diss['marks9'],diss['marks10'],diss['marks11'],diss['marks12'],diss['marks13'],diss['marks14'],diss['marks15'],diss['marks16'],diss['marks17'],diss['marks18'],diss['marks19'],diss['marks20'])      
  
                #query = 'INSERT INTO quiz(pk,name,mone,mtwo,mthree,mfour,mfive,msix,mseven,meight,mnine,mten) VALUES ("%s", "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (pk,na,dis['marks1'],dis['marks2'],dis['marks3'],dis['marks4'],dis['marks5'],dis['marks6'],dis['marks7'],dis['marks8'],dis['marks9'],dis['marks10'])
                c.execute(query)
                conn.commit()
        except KeyError:
             st.warning("Please Login")
        except MySQLdb.IntegrityError:
             st.warning("Already Submitted")
    
        except UnboundLocalError:
            st.warning("Please answer all questions")    
        
 #CREATE TABLE survey (pk int PRIMARY KEY,name varchar(100),mone int,mtwo int,mthree int,mfour int,mfive int ,msix int,mseven int,meight int,mnine int,mten int,meleven int,mtwelve int,mthirteen int , mfourteen int,mfifteen int,msixteen int, mseventeen int, meighteen int,mnineteen int,mtwenty int);
 #query = 'INSERT INTO quiz(pk,name,mone,mtwo,mthree,mfour,mfive,msix,mseven,meight,mnine,mten,meleven,mtwelve,mthirteen, mfourteen,mfifteen,msixteen, mseventeen, meighteen,mnineteen,mtwenty) VALUES ("%s", "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (pk,na,diss['marks1'],diss['marks2'],diss['marks3'],diss['marks4'],diss['marks5'],diss['marks6'],diss['marks7'],diss['marks8'],diss['marks9'],diss['marks10'],diss['marks11'],diss['marks12'],diss['marks13'],diss['marks14'],diss['marks15'],diss['marks16'],diss['marks17'],diss['marks18'],diss['marks19'],diss['marks20'])      
    
    if st.button("Check your result", key='result'):
        
        try:
            with st.spinner(text ="DyslexiaML is Analyzing"):
                pred = prediction(user_prime_key = pk)
                if int(pred) == 2:
                    st.balloons()
                    st.success("Your Child Does Not Has Dyslexia!! ")
                elif int(pred) == 1:
                    st.success("Your Child Has Mild Dyslexia Symptoms. Consult Doctor ")
                else:
                    st.success("Your Child Has Dyslexia Symptoms. Consult Doctor ")
        except UnboundLocalError:
            st.warning("Please Login")    
        

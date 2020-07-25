import pandas as pd 
import numpy as np
import streamlit as st
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
import MySQLdb



def fetchData():
    try:
        conn = MySQLdb.connect("localhost","ryan","mark50","dyslexia" )
        c = conn.cursor()
    except:
        print('Cant establish connecetion, Database Server Down!')
        
    dfquiz = pd.read_sql_query("select * from quiz;", conn)
    dfsurvey = pd.read_sql_query("select * from survey;", conn)
    return dfquiz,dfsurvey


def result(user_prime_key=None):
    dfquiz,dfsurvey = fetchData()
    result = pd.merge(dfquiz, dfsurvey, on=['pk', 'name'], suffixes=['_quiz', '_survey']) #this will have complete reuslt
    temp = result[result.pk == user_prime_key] #user specific results in the session
    return temp

def domainmarks(dataframe=None):
    temp1 = dataframe.drop(['name','pk'],axis=1)
    marksdf = pd.DataFrame(columns=(['Language_vocab', 'Memory', 'Speed','Visual_discrimination','Audio_Discrimination', 'Survey_Score']) )
    marksdf.Language_vocab = (temp1.mone_quiz+temp1.mtwo_quiz+temp1.mthree_quiz+temp1.mfour_quiz+temp1.mfive_quiz+temp1.msix_quiz+temp1.meight_quiz)/24
    marksdf.Visual_discrimination = (temp1.mone_quiz+temp1.mthree_quiz+temp1.mfour_quiz+temp1.msix_quiz)/16
    marksdf.Memory = (temp1.mtwo_quiz+temp1.mnine_quiz)/8
    marksdf.Audio_Discrimination = (temp1.mseven_quiz+temp1.mten_quiz)/8
    marksdf.Speed = np.random.uniform(0,1)
    surevy_col =['mone_survey', 'mtwo_survey', 'mthree_survey', 'mfour_survey',
       'mfive_survey', 'msix_survey', 'mseven_survey', 'meight_survey',
       'mnine_survey', 'mten_survey', 'meleven', 'mtwelve', 'mthirteen',
       'mfourteen', 'mfifteen', 'msixteen', 'mseventeen', 'meighteen',
       'mnineteen', 'mtwenty']
    marksdf.Survey_Score = temp1[surevy_col].sum(axis=1)/80
    data = marksdf.copy()
    del temp1
    del marksdf
    return data
 
 
def model(user_prime_key=None):
    res = result(user_prime_key = user_prime_key)
    
    data = domainmarks(res)
     
    print("loading model")
    pipeline = joblib.load('transform_predict.joblib') #url
    print('Done')
    
    predictions = pipeline.predict(data)
    #print(predictions[0])
    return predictions[0]

# def main():
#     user_prime_key=1
#     print(model(user_prime_key= user_prime_key)) 

# if __name__ == "__main__":
#     main()

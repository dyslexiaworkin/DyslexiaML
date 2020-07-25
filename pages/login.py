import streamlit as st
from pages.fetch import*

import pandas as pd
import hashlib

import MySQLdb

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


def create_usertable(c):
	pass # user will have to create it once
	#CREATE TABLE tweets (id int AUTO_INCREMENT PRIMARY KEY,  username varchar(50)prediction int(1),password varchar(256)prediction int(1),response_status int(1));
	#CREATE TABLE login (id int AUTO_INCREMENT PRIMARY KEY,  username varchar(100),password varchar(256));

def add_userdata(username,password,c,conn):
    query = 'INSERT INTO login(username,password) VALUES ("%s","%s");' % (username,password)
    c.execute(query)
    conn.commit()

def login_user(username,password,c):
	c.execute('SELECT * FROM login WHERE username = %s AND password = %s',(username,password))
	data = c.fetchall()
	return data


def view_all_users(c):
	c.execute('SELECT * FROM login')
	data = c.fetchall()
	return data




# def insert_(tweet,username,pnr,prediction,tweet_id):
#      query = "INSERT INTO tweets(tweet,username,pnr,prediction,tweet_id) VALUES ('"+tweet+"','"+username+"',"+str(pnr)+","+str(int(prediction))+","+str(tweet_id)+");"
#     try:
#         conn = MySQLdb.connect("localhost","ryan","mark50","twitter" )
#         cursor = conn.cursor()
#         cursor.execute(query)
#         print("Database insertion SUCCESSFUL!!")
#         conn.commit()
#     except MySQLdb.Error as e:
#         print(e)
#         print("Database insertion unsuccessful!!")
#     finally:
#         conn.close()



login_dict = {}
name_dict = {}
def main():
    #global PRIMARY_KEY 
	"""Simple Login App"""
	#front_up()
	st.title("Login/SignUp")

	menu = ["Login","SignUp"]
	choice = st.selectbox("Menu",menu)
	try:
    		conn = MySQLdb.connect("localhost","ryan","mark50","dyslexia" )
    		c = conn.cursor()
	except:
		st.error('Cant establish connecetion, Database Server Down!')
	
	
	if choice == "Login":
		st.subheader("Login Section")

		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')
		if st.button("Login"):
			
			
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd),c)
			
			if result:
				#st.write(result[0][0])
				PRIMARY_KEY = result[0][0]
				name_dict.update({'name':result[0][1]})
				login_dict.update({'key':PRIMARY_KEY})
				#session_state.p = PRIMARY_KEY
				st.success("Logged In as {}".format(username))
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			
			add_userdata(new_user,make_hashes(new_password),c,conn)
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")




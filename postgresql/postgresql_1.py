#in this module  we will learn how to connect to postgresql database
import psycopg2 #this modeule  is used to connect to postgresql database

#establishing the connection
connect = psycopg2.connect(dbname="postgres", user="postgres", password="2611", host="localhost", port="5432")

#checking if the connection is established
print("Connection established")
# in this module  we  will learn how to insert data into the table
import psycopg2  # this module is used to connect to postgresql database


def table():
    # establishing the connection
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="2611",
        host="localhost",
        port="5432"
    )

    # checking if the connection is established
    print("Connection established")

    # creating a cursor object using the cursor() method
    cursor = connect.cursor()

    # creating table as per requirement
    cursor.execute('''CREATE TABLE employee(
        name TEXT,
        age INT,
        salary INT
    )''')

    print("Table created")

    # commit your changes in the database
    connect.commit()   # ✅ commit is called on the connection, not cursor
    print("Changes committed")

    # closing the connection
    connect.close()
    print("Connection closed")

def data():
    # establishing the connection
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="2611",
        host="localhost",
        port="5432"
    )
    # checking if the connection is established
    print("Connection established")

    # creating a cursor object using the cursor() method
    cursor = connect.cursor()

    # creating table as per requirement
    cursor.execute('''insert into employee(name, age, salary) values('John', 25, 50000)''')

    print("Data inserted")

    # commit your changes in the database
    connect.commit()   # ✅ commit is called on the connection, not cursor
    print("Changes committed")

    # closing the connection
    connect.close()
    print("Connection closed")

#data extraction
def extract():
    # establishing the connection
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="2611",
        host="localhost",
        port="5432"
    )
    # checking if the connection is established
    print("Connection established")

    # creating a cursor object using the cursor() method
    cursor = connect.cursor()

    # creating table as per requirement
    cursor.execute('''select * from employee''')
    print(cursor.fetchall())

    print("Data extracted")

    # commit your changes in the database
    connect.commit()   # ✅ commit is called on the connection, not cursor
    print("Changes committed")

    # closing the connection
    connect.close()
    print("Connection closed")
    
extract()
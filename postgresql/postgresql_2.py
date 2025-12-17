import psycopg2  # this module is used to connect to postgresql database

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
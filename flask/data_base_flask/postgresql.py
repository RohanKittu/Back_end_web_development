import psycopg2

'''
In the below connect function please enter your following details
dbname :- enter database name
user :- enter your user ID
password :- Enter your password
host :- enter your host ID
'''

#starting the session
conn=psycopg2.connect("dbname=chatbot user=rohanvarma password=Kittu@201995 host=127.0.0.1")
'''
cursor the command or vessel by which we communicate with the data bases.
There are two types of cursor 
1) client side cursor.
2) server side cursor.

1)client side cursor :- are when you quary ,the client will allocate the memory to the entire dam thing that we are quaring.so basically we entirly pull the into our little application.
2)server side cursor :- This means ,dont send entire information at once,when ever needed we quary from the server.
'''

'''
using the exception handling for smooth running of code ,even if the program throws error.
'''
try:
    #creating the cursor
    cur=conn.cursor()
    #checking if the data base is connected or not
    if(cur):
        print("connected")
    else:
        print("disconnected")

    #executing few commandes through cursor.

    #cur.execute("select * from detail")
    cur.execute("select * from trail")
    #fetching the rows from the table demo3 from database
    rows = cur.fetchall()
    #printing all the rows from the tables.
    print("\nThese are the rows present in the table :- ")
    print(rows)
    #printing all the rows
except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        print("closing the connection")
        cur.close()
        conn.close()
'''
Note you should always close the connection and cursor.
'''
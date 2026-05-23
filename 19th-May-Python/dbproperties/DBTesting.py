import DBConnection

query="SELECT * FROM users"
db= DBConnection()
connection= db.get_connection()
try:

    result= connection.execute(query)
    print(result)
finally:
    connection.close()
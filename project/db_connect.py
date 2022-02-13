import psycopg2

# Enter dbname, user and password
def connect_db():
    conn = psycopg2.connect("dbname= user= password=")
    return conn

     
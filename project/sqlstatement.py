
# STATEMENTS FOR VAULT TABLE
# insert, update , delete
def insert_db_vault():
    query = """insert into vault values (%s, %s, %s);"""
    return query

def update_db_username():
    query = """update vault set username = %s where company = %s"""
    return query

def update_db_password():
    query = """update vault set cpasswd = %s where company = %s"""
    return query

def delete_db_vault():
    query = """delete from vault where company = %s"""
    return query

# select one field
def select_db_query():
    query = """select * from vault where company = %s"""
    return query

# select entire vault
def select_db_vault():
    query = """select * from vault"""
    return query


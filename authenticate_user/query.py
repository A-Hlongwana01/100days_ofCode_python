import sqlite3

def myQuery(credentials):
    # connecting to database
    conn = sqlite3.connect("database.db")

    # creating a cursor
    c = conn.cursor()

    # creating table if it does not already exist
    c.execute("CREATE TABLE IF NOT EXISTS creds(id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

    #adding data to table
    c.execute("""
        INSERT INTO creds("username","password") VALUES(
            ?,?
        )
    """,credentials)

    
    conn.commit()
    conn.close()

    
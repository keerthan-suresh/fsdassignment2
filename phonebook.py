import sqlite3
try:
    conn = sqlite3.connect("records.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE user2 (id INTEGER, name TEXT, cell BIGINT, email TEXT)")
    cur.execute("""INSERT INTO user2 VALUES (1, 'Keerthan', 9945243336, 'kes21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (2, 'Aryan', 9254260579, 'ary21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (3, 'Vikram', 9112230698, 'vik21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (4, 'Aditya', 9163190521, 'adi21ec@cmrit.ac.in')""")
    cur.execute("""INSERT INTO user2 VALUES (5, 'Arjun', 9932592523, 'arj21ec@cmrit.ac.in')""")
    conn.commit()
    print("Insert operation done")

    data=cur.execute("""SELECT * FROM user2""") 
    for row in data: 
        print(row)

except sqlite3.Error as e:
    print("Error while inserting Data", e)

finally:
    if(conn):
        conn.close()
        print("Connection closed")
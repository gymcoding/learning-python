import sqlite3
con = sqlite3.connect('./commit.db')
cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
cur.execute("INSERT INTO PhoneBook VALUES('Someone', '010-5670-2343');")
cur.execute("INSERT INTO PhoneBook VALUES('Soryong', '010-2780-4567');")
con.commit()
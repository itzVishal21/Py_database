import sqlite3  
  
#conn = sqlite3.connect(':memory:')  
conn = sqlite3.connect('vishal.db')  

c = conn.cursor()


c.execute("SELECT * FROM Movies")
items = c.fetchall()
for item in items:
    print(item)

print('The movies of Akshay Kumar are')    

c.execute("SELECT * from Movies Where actor='Akshay Kumar'")
names = c.fetchall()
for name in names:
    print(name)

print('The movies of Ajay Devgn are')    

c.execute("SELECT * from Movies Where actor='Ajay Devgn'")
names = c.fetchall()
for name in names:
    print(name)


conn.commit()
conn.close()

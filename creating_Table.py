import sqlite3  
  
#conn = sqlite3.connect(':memory:')  
conn = sqlite3.connect('vishal.db')  

c = conn.cursor()

c.execute('''CREATE TABLE Movies (
    name text, 
    actor text,
    actress text, 
    director text, 
    year of release int)

'''


)
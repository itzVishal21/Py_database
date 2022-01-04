import sqlite3  
  
#conn = sqlite3.connect(':memory:')  
conn = sqlite3.connect('vishal.db')  

c = conn.cursor()

my_Movies = [
                ('Shershaah','Sidharth Malhotra','Kiara Advani','Vishnuvardhan','2021'),
                ('Sooryavanshi', 'Akshay Kumar', 'Katrina Kaif', 'Rohit Shetty', '2021'),
                ('Tanaji', 'Ajay Devgn', 'Kajol', 'Om Raut', '2020'),
                ('Good News','Akshay Kumar','Kareena Kapoor','Raj Mehta','2019'),
                ('War','Hritik Roshan', 'Vaani Kapoor', 'iddharth Anand','2019')
                
            ]
c.executemany("INSERT INTO Movies Values (?,?,?,?,?)",my_Movies)
print('Record added')


conn.commit()
conn.close()
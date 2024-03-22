import sqlite3

conn = sqlite3.connect('FamPrac.db')
cursor = conn.cursor()

cursor.execute("CREATE Table Family(FamilyId integer primary key, Father_Name Text, Mother_Name Text)")
cursor.execute("INSERT INTO Family Values(1,'Will Smith','Jada Smith')")
cursor.execute("INSERT INTO Family Values(2,'Billy Cyrus','Tish Cyrus')")
cursor.execute("INSERT INTO Family Values(3,'Barack Obama','Michelle Obama')")
cursor.execute("INSERT INTO Family Values(4,'Bill Gates','Melinda Gates')")


cursor.execute("CREATE Table Kids(KidId integer primary key, Name Text, Age integer, FamilyId integer)")
cursor.execute("Insert INTO Kids Values(1, 'Jaden Smith', 21, 1)")
cursor.execute("Insert INTO Kids Values(2, 'Willow Smith', 19, 1)")
cursor.execute("Insert INTO Kids Values(3, 'Miley Cyrus', 26, 2)")
cursor.execute("Insert INTO Kids Values(4, 'Malia Obama', 21, 3)")
cursor.execute("Insert INTO Kids Values(5, 'Sasha Obama', 18, 3)")
cursor.execute("Insert INTO Kids Values(6, 'Justin Bieber ', 18, 5)")

cursor.execute("SELECT Name, Mother_Name FROM Kids LEFT JOIN Family ON Kids.FamilyId = Family.FamilyId")
users = cursor.fetchall()
for row in users:
    print(row)

#cross join : used to join two tables without any specific matching patterns
#Inner join : used to join specific rows with similar values from two tables 
#Left join : used to join rows from the left of second table regardless of if they match the right side and for the table on right you get the matching rows that only match the right
#Right join : used to join rows from the Right of second table regardless of if they match the left side and for the table on right you get the matching rows that only match the left


conn.commit()
conn.close()
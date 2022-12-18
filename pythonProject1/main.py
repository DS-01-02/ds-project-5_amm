# importing psycopg2 module
import psycopg2

# establishing the connection
n=int(input("insert : 1\t remove : 2\t print info : 3\t sort by name : 4"))

conn = psycopg2.connect(
    database="test",
    user='postgres',
    password='Mohammad#*127*#',
    host='localhost',
    port='5432'
)

# creating a cursor object
cursor = conn.cursor()

# creating table

if n ==1 :
    data = [('file1', '2022','pdf'), ('file2', '2021','mp4'),
        ('file3', '2020','zip'), ('file4', '1957','mp3'),
        ('file5', '2018','zip'),("file6","2022","zip")]



    for d in data:
        cursor.execute("INSERT into FolderInfo(name, date,type) VALUES (%s, %s,%s)", d)

    print("List has been inserted to employee table successfully...")

# Commit your changes in the database
    conn.commit()
elif n==2:
    m =input("file name : \n")
    cursor.execute("delete from folderinfo where name = %s",(m,))
    conn.commit()

elif n ==3:
    cursor.execute("select * from folderinfo")

    data = cursor.fetchall()
    conn.commit()
    for d in data:
        print (d)
elif n==4:
    cursor.execute("select * from folderinfo order by name")

    data = cursor.fetchall()
    conn.commit()
    for d in data:
        print(d)

# Closing the connection"
conn.close()
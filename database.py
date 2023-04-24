import sqlite3  
  
conn = sqlite3.connect('example.db')  
print ("Opened database successfully");
conn.execute('''CREATE TABLE EMPLOYEE11 (FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT,SEX CHAR(1),INCOME FLOAT )''')  
print ("Table created successfully");  
conn.execute("INSERT INTO EMPLOYEE11(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('RAJESH','GANGULY',28,'M',93776)");  
  
conn.execute("INSERT INTO EMPLOYEE11(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('SACHIN','TENDULKAR',40,'M',98463)");  
  
conn.execute("INSERT INTO EMPLOYEE11(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('ANIL','KUMBLE',42,'M',64300)");  
  
conn.execute("INSERT INTO EMPLOYEE11(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('RAHUL','DRAVID',39,'M',84300)");  
  
conn.commit()  
print ("Records inserted successfully");
data = conn.execute("select * from EMPLOYEE11");  
  
for row in data:  
 print ("FIRST_NAME = ", row[0])  
 print ("LAST_NAME = ", row[1])  
 print ("AGE = ", row[2])  
 print ("SEX = ", row[3])
 print ("INCOME = ", row[4])

conn.execute("UPDATE EMPLOYEE11 SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M'))
conn.commit()
data = conn.execute("select * from EMPLOYEE11");
print("Updated table");
  
for row in data:  
 print ("FIRST_NAME = ", row[0])  
 print ("LAST_NAME = ", row[1])  
 print ("AGE = ", row[2])  
 print ("SEX = ", row[3])
 print ("INCOME = ", row[4])
conn.execute("DELETE FROM EMPLOYEE11 WHERE AGE > '%d'" % (40))
conn.commit()
data = conn.execute("select * from EMPLOYEE11");
print("After deletion")
  
for row in data:  
 print ("FIRST_NAME = ", row[0])  
 print ("LAST_NAME = ", row[1])  
 print ("AGE = ", row[2])  
 print ("SEX = ", row[3])
 print ("INCOME = ", row[4])

conn.close()  

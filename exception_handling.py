ch=1
while ch==1 or ch==2 or ch==3: 
  print("\n\n\n1.File handling error") 
  print("2.Divide by Zero Exception") 
  print("3.Assert Function") 
  print("4.Exit")
  ch=int(input("Select your choice :")) 
  if ch==1:
    try:
      fh = open("testfile", "r") 
      fh.write("Test document")
    except IOError:
      print("File handling error") 
    else:
      print("Written content in the file successfully") 
      fh.close()
  elif ch==2: 
    try:
      a=int(input("Enter a for a/b : ")) 
      b=int(input("Enter b for a/b : ")) 
      print("Result : ",a/b)
    except ZeroDivisionError: 
      print("Divide by Zero Exception")
  elif ch==3: 
    marks=[]
  for i in range(0,3): 
    marks.append(int(input("Enter marks : ")))
  sum1=0
  for i in marks:
    assert (i>=35),"Fail" 
    sum1=sum1+i
print("Percentage = ",sum1/3)

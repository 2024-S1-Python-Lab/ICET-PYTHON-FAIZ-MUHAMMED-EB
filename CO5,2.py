filename1=input("enter source file:")
with open(filename1,'r')as file1:
    lines=file1.readlines()
filename2=input("enter destination file:")
with open(filename2,'w')as file2:
  for i in range(len(lines)):
    if i%2==0:
      file2.write(lines[i])
with open(filename2,'r')as file2:
         lines=file2.readlines()
print("lines from the file:",lines)      
    
               
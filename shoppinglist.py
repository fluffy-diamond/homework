file=open("filehandling2.txt","x")
file.close()

file=open("filehandling2.txt","w")
file.write("Apples\n")
file.write("mangoes\n")
file.write("bread\n")
file.close()

file=open("filehandling2.txt","r")
print(file.read())
file.close()

file=open("filehandling2.txt","a")
file.write("chocolate\n")
file.close()

file=open("filehandling2.txt","r")
print(file.read())
file.close()

file=open("filehandling2.txt","r")
print("No. of items:",len(file.readlines()))
file.close()
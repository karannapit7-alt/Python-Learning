# open for reading (default)

f = open("demo.txt","r")
 
data = f.read()

print(data)

f.close()


# open for Writing, truncating the file first.

f = open("demp.txt","w")

f.write("i am karan thakur ")

f.close()

# open for writing. appending to the end of the file if it exists

f = open("demo.txt","a")

f.write("you are very good boy , you are everyday coding")

f.close()





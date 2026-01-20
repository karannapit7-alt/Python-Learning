# Create a new File "Practice.txt" using python. 

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file i/o\nusing java\nI like programming in java.")
    
    

# WAF that replace all ocurrense of "Java" with "python" in above file.

def replace_file():
    with open("practice.txt","r") as f:
        data = f.read()
        new_data = data.replace("java","Python")
        print(new_data)
         
replace_file()

# Search if the word "learning" exists in the file or not.

word = "learning"

with open("practice.txt","r") as f:
    data = f.read()
    if(word):
        print("Found")
    else:
        print("Not Found")
        
        
# WAF to find in which line of the file does the word "learning" occur first. print -1 word not found.

def check_line():
    word = "learning"   
    data = True
    line = 1
    with open("practice.txt","r") as f:
         while data:
            data = f.readline()
            if(word in data):
                print(line)
                return
            line += 1
    return -1 
print(check_line())

# From a file containing numbers separated by comma , print the cont of a numbers.

count = 0
with open("practice_count.txt","r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    for i in nums:
        if(int(i) % 2 == 0):
            count +=1
print(count)
    
        

    
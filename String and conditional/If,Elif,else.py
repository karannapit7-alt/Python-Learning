#if
light = "red"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "blue"):
    print("wait")

#Elif
light = "red"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "blue"):
    print("wait")

#Else:
age = 14

if(age >= 18):
    print("vote apply")
else:
    print("cannot vote apply")
    
#Grade students based on marks
marks = int(input("Enter the value"))

if(marks >= 90): 
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "c"
else:
    grade = "D"
    
print("Grade students based on marks",grade)

marks = 94

if(marks >= 90 ):
    grade = 'A'
elif(marks >= 80 and marks < 90 ):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = 'C'
else:
    grade = 'D'
print("grade students based on marks",grade)


    
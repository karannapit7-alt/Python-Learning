# found any char in a string using for loop.

str = " Hello sir i am karan thakur "  #string declaration 
for char in str:
    if char == 's':
        print("sir found in the string")   #print if found
        break
    print(char)
else:
        print("sir not found in the string")  #print if not found
        
        
# one more practice same problem
str = "K A R A N T H A K U R"                  #string declaration 
for char in str:   
    if char == 'H':                            #check for char H
        print("H found in this string")
        break                                  #break the loop if found 
    print(char)
else:
     print("H not found in this string")
     
     

# using for loops 

# print the elements of the follwing list using a loop.
          #[1,4,9,16,25,36,49,64,81,100]
          
nums = [ 1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)   # This will print each element in the list.
    
    
# search for an element in the following tuple using a loop.
           #(2,3,4,5,6,52,30,89,63,48,10,63)
           
nums = (2,3,4,5,6,52,30,89,63,48,10,63)  # one most important ponit is linear search. 
x = 63

idx = 0
for el in nums:
    if el == x:
        print("number found at index", idx)  # This will print the index where the number is found. 
        break
    idx += 1
else:
    print("number not found")    
    
    
# for loops for i in range start , end.

for i in range (1 ,10):
    print(i)     # print number from 1 to 10 but not print 10 last number. why because range function is exclusive of last number.          
    
    
# for loops for in range start , end , step.

for i in range (1,101,5):
    print(i)   # print number from 1 to 101 with step 5.
    
# print numbers for 100 to 1 using for loop and range function.

for i in range (100,0,-1):  # starting from 100 to 1 with step -1.
    print(i)    
    
# print even number from 1 to 200 using for loop and range function.

for i in range (2,201,2): # starting from 2 to 200 with step 2.
    print(i)    # print even number from 1 to 200.
    
    
# print odd number from 1 to 100 using for loop and range function.

for i in range (1,100,2):  # starting from 1 to 100 with step 2.
    print(i)  # print odd number from 1 to 100.
    
    
# print the multiplication table of a number using for loop and range function.

n = int(input("Enter a number to print its multiplication table: "))  # taking input from user.

for i in range(1,11):
    print(n*i)      # print the multiplication table of the numbner.
    
    
# print 100 time sorry using for loop and range function.

for i in range(101):   
    print("cse Ai&ml")
    
    
# WAP to find the sum of first n natural number using for loop and range function.

#n = 6
n = int(input("enter a number "))

sum = 0
for i in range(1,n + 1): # range function is exclusive of last number so we use n+1.
    sum += i
print("Total sum is :- ", sum)

# WAP to find the sum of first n natural number using while loop.

num1 = int(input("enter a number"))

sum = 0
i = 1
while i <= num1:   # initialize i
    sum += i  
    i += 1
print("Total sum is :- ",sum)



# WAP to find the factorial of a number using for loop and range function.

num1 = int(input("enter a number"))

fact = 1
for i in range(1,num1 + 1):    # range function is exclusive of last number so we use n+1.
    fact = fact * i
print("Factorial of ",fact)
    
    
    
# print number from 1 to 100.

i = 1
while i <= 100:
    print(i)
    i += 1
    
# print number from 100 to 1. 
   
i = 100
while i>= 1:
    print(i)
    i -= 1
    
# print table of 7.
    
i = 1
while i <= 10:
    print(7 * i)
    i += 1
    
#print table n.
    
n = int(input("Enter a number:"))
i = 1
while i<= 10:
    print(n * i)
    i += 1

    
#print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1
    
# find the index of number 36 in the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
    
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 1
while i <= len(nums):
    if nums[i-1] ==x:
        print("found at index", i)
    i += 1
          
     



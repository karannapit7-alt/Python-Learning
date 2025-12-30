# challenge 1:- 

my_slicing = "PYTHON-PROGRAMMING" #
print(my_slicing[0:6])
print(my_slicing[::-1])


# challenge 2:-
nums = [10,25,33,40,55]

for i in nums:
    print(i)
    i += 1
    
nums = [10,25,33,40,55]

for i in nums:
    if i % 2 ==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
        
# challenge 3:- 
student_data ={ 
               "name": "karan","marks": 85}
if student_data["marks"] >= 80:
    print(f"{student_data["name"]} has passed the exam")
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movies = []
mov1 = input("Enter the 1st mov ")
mov2 = input("Enter the 2nd mov")
mov3 = input("Enter the 3rd mov")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# WAP to check if a list contains a palindrome of elements. (hint: use copy() method).
my_list = [1,2,1,]

list_copy = my_list.copy()
list_copy.reverse()

if(list_copy == my_list):
    print("palindrome")
else:
    print("NOT Palindrome") 
    
# WAP to count the number of students with the "A" grade in the folling tuple.
grade = ("C","D","A","A","A","B","B","A")
print(grade.count("A"))

#store the above values in a list & sort then from "A" to "3".

list = ["C","D","B","A"]
list.sort()
print(list)


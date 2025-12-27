#list Example
marks = [80,30,52,63,85,65,45,20]  # 
print("marks of student:-",marks)
print(type(marks))

name = ["Kamlesh thakur","Arjun thakur","parmila devi","Karan thakur"]
print("Name of very imporant person:-",name)
print(type(name))

#index values 
gadi = [7837,8018,1817,2961]
print(gadi[1])

#length list
number = [520,6320,485,2,3,4,5]
print(len(number))

#list 
my_list = [2,4,3,9,10,42,39,24,56]
print(my_list)

#wap 2 raplace 100
my_list = [2,4,3,9,10,42,39,24,56]
my_list[3] = 100
print(my_list)
del my_list[4]
print(my_list)

# ek user se input lena hain aur 3 friend ke name usme store karna hain aur print karna hain
friend = []
 
friend1 = input("enter your first friend1 name :")
friend2 = input("enter your second friend name :")
friend3 = input("enter your third friend name :")


'''print("your friend1 name is :",friend1)
print("your friend2 name is :",friend2)
print("your friend3 name is :",friend3)'''    # yah bina empty list ke print karne ka tarika hain .

friend.append(friend1)
friend.append(friend2)
friend.append(friend3)
print("your friend list is:",friend)      # yah empty list ke sath print karne ka tarika hain.
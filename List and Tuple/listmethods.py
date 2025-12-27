#list.Append
my_list = [85,65,120,320,45,'karan',6] # this code adds 52 at the end of the list.
my_list.append(52)
print(my_list)

#list.sort
my_list = [20,85,1,3,60,65]  # This code sorts the list in asscending order.
my_list.sort()
print(my_list)

#list.sort(reverse=True)
my_list = [20,85,1,3,60,65]   # This code sorts the list in descensing order. 
print(my_list.sort(reverse=True))
print(my_list)

#list.reverse 
my_list = ["thakur","kumar","karan"]  # This code reverses the order of the list elements.
my_list.reverse()
print(my_list)

#list.insert
my_list = ["karan","kumar","thakur"]  # This code inserts 20 at index 1.
my_list.insert(1,20)
print(my_list)

#list.remove
my_list = [1,5,6,8,9]  # This code removes 5 from the list.
my_list.remove(5)
print(my_list)

#list.pop
my_list = [52,1,78,96,85]  # This code removes the element at index 3.
my_list.pop(3)
print(my_list)


#List slicing.
my_list = [52,20,1,3,5,2,6,4,3]  # This code demonstrates various ways to slice a list.
print(my_list[1:6])
print(my_list[:6])
print(my_list[1:])
print(my_list[-3:-1])

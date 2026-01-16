# print n to 1 backwards

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(6)



# Write a recursive function to calculate the sum of first n natural number.

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(5)
print(sum)


# Write a Recursive function to print all elements in a list.

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

Fruits = ["mango","Banana","watermelon","apple"]

print_list(Fruits)

    


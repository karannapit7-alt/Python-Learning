# This function calculates the sum of two numbers

def calc_sum(a,b):  
    return a + b    
sum = calc_sum(5, 10)    # call the function and store the result.
print("The sum is:", sum) 

# This function calculates the average of 3 numbers.

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(20,45, 56)   # call the function but not storing the result.
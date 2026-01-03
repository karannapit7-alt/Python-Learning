# WAF to print the lenght of a List. (list is the parameter)

state = ["Delhi","Jharkhand","mumbai","Kolkata","pune","Kerla"]
Laptop = ["HP","Dell","Apple","intel","micro"]

def print_len(list):
    print(len(list))
    return list
print_len(state)
print_len(Laptop)


# WAF to print the elements of a list in a single line. (list is the parameter)

company = ["TCS","Wipro","Google","Microsoft","HCL Tech"]

def print_list(list):
    for item in list:
        print(item, end = " ")
    
print_list(company)
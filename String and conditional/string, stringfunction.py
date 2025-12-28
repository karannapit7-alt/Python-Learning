# string is data type that is used a squence of characters. 


# string are defined in python by either using single quotes or double quotes.

str1 = "This is a string"
str2 = 'this is also a string'
str3 = '''This is a multi line string'''

print(str1)
print(str2)
print(str3)

# print string add
str1 = "karan"
str2 = "thakur"
final_str = str1 + str2

print(final_str)  # it will print karanthakur
print(len(final_str))


# string indexing and slicing.

my_str = "Hello, welcome to karan python code "   # indexing is start from 0 to n-1.
print(my_str[0])
print(my_str[1])
print(my_str[2])
print(my_str[3])
print(my_str[4])

# slicing any postive index string.
my_str = "PYTHONPROGRAMMING"   
print(my_str[0:3])
print(my_str[:5])
print(my_str[3:7])
print(my_str[5:9])
print(my_str[7:12])

# slicing any negative index string.
my_str = "PYTHONPROGRAMMING"
print(my_str[-1:-5])   # it will not print anything because in negative slicing the start index should be less than end index.
print(my_str[-5:]) 
print(my_str[-10:-5])
print(my_str[-12:-7])
print(my_str[-15:-10])


# String functions/methods.

str1 = "I am a coder"

print(str1.upper())     # it will convert all the characters to upper case.
print(str1.endswith("coder"))
print(str1.replace("coder","developer"))
print(str1.split(" "))   # it will split the string at space and return a list of words.
print(str1.find("count"))





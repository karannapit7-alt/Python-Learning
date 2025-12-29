# basic Dicte 
Dict = {
    "name" : "karan",
    "Age" : 52,
    "Coures" : "CSE"
}

print(Dict)

#Dict Mutable
Dict = {
    "name" : "Thakur",
    "Age" : 52,
    "roll" : 562 
} 

Dict["name"] = "Karan"
Dict["marks"] = 532
print(Dict)

# NUll Dict
Null_dict = {}
Null_dict["Name"] = "kamlesh"
print(Null_dict)

#Nested Dictioaries 
student = {
    "name" : "karan",
     "subject" : {
        "phy" : 98,
        "chem" : 99,
        "math" : 99.5        
    }
}

print(student["subject"])
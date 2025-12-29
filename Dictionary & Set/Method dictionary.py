#mydict.key()
Dict = {
    "name" : "karan",
    "age" : 52,
    "marks" : 785,
    "subject" : "maths"
}

print(Dict.keys())

# dict.value
Dict = {
    "name" : "karan",
    "age" : 56,
    "marks" : 895,
    "subject" : "English"
}

print(Dict.values())

# Dict.items
Dict = {
    "name" : "karan",
     "subject" : {
         "maths" : 852,
         "english" : 895,
         "mathematices" : 963
         
     }
}

print(Dict.items())

# Dict.get
Dict = {
    "name" : "karan thakur",
    "subject" : {
        "maths" : 452,
        "social media" : "best",
        "English" : 785
    } 
}

print(Dict.get("name"))
print(Dict["name"])
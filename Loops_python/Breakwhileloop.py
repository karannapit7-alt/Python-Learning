# Break 
i = 1
while i <= 20:
    print(i)
    if(i == 13):
        break
    i += 1
    
#continue odd print 
i = 1 
while i <=10:
    if(i%2 == 0):
         i +=1 
         continue
    print(i)
    i += 1
    
#continue even print 
i = 1
while i <= 10:
    if(i%2 != 0):
         i += 1 
         continue
    print(i)
    i += 1
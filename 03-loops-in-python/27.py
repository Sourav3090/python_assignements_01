text= "if you think you can not do, you can not show think wisely "
count = 0
final =""
for i in text:
    if i != " ":
        final+=i
    else:
        if count%2==0:
            print(final,end=" ") 
        final=""
        count+=1   
    
        
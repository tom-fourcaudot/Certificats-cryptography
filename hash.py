def hash (message : str)-> str:
    hashMess = ""
    nbEven = 0

    for c in message :
        val = int(c)
        val = int(val*13/2)
        hashMess += str(val) 
    
    for c in message :
        val = int(c)
        if (val % 2) == 0 :
            nbEven += 1
    
    hashMess += str(nbEven)
    hashMess = hashMess.replace("0","")
    return hashMess

message = "8135758"
print(hash(message))
message = '2052'
print(hash(message))
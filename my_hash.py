def my_hash (message : str)-> str:
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
    size = len(hashMess)
    tmp = ""
    for i in range(size):
        tmp += str(int(hashMess[i])*size)
        if size < 20:
            size = len(hashMess) + len(tmp) - 1
        else:
            size = 20

    hashMess = tmp
    return hashMess

message = "2052"
print(my_hash(message))
message = "2052"
print(my_hash(message))
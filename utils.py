'''
Take a message ( int ) and transform it into list
exemple : 123 -> [1, 2, 3]
@param msg : the message
@return : the list
'''
def int2lst(msg: int)-> list:
    return [int(c) for c in str(msg)]

'''
Take a message (list of int) and transform into a key
@param msg : the message
@return : the key
'''
def msg2pb_key(msg: list)-> tuple:
    lenE = msg[0]
    msg = [str(c) for c in msg[1:]]
    return (int(''.join(msg[:lenE])), int(''.join(msg[lenE:])))

'''
Take a key and transform it into a message (list)
The first element of the message will be the len of the first part of the key
exmeple (8, 447) -> [1, 8, 4, 4, 7]
here, the 1 mean that the first part of the key (e or d) have a len of 1
@param key ; the key to transform
@return : the message ( list of int )
'''
def create_message(key: tuple)-> list:
    lenE = len(str(key[0]))
    message = [lenE]
    message+=(int2lst(key[0]))
    message+=(int2lst(key[1]))
    return message
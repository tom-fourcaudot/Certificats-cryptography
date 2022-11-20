def int2lst(msg):
    return [int(c) for c in str(msg)]

def msg2pb_key(msg):
    lenE = msg[0]
    msg = [str(c) for c in msg[1:]]
    return (int(''.join(msg[:lenE])), int(''.join(msg[lenE:])))

def create_message(key):
    lenE = len(str(key[0]))
    message = [lenE]
    message+=(int2lst(key[0]))
    message+=(int2lst(key[1]))
    return message
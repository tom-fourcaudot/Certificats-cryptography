import hashlib
import utils
import keygen as kg

HASH_LEN = 4 # fixed len of hash message

'''
Encrypt a message ( list of int ) with a key
@param key : the Crypt key
@param msg : the msg to encrypt
@return : the crypt message ( list of int )
'''
def crypt(key:tuple, mess:list)->list:
    e, n = key
    res = []
    for c in mess:
        tmp = pow(int(c), e, n)
        res.append(tmp)
    return res

'''
Decrypt a message ( list of int ) with a key
@param key : the decrypt key
@param msg : the msg to decrypt
'''
def decrypt(key:tuple, mess:list)->list:
    d, n = key
    res = []
    for c in mess:
        tmp = pow(c, d, n)
        res.append(tmp)
    return res

'''
Hash a message, with a len of HASH_LEN
@param msg : the message to hash
@return : the hashed message
'''
def hash_mess(msg:str)->int:
    hash_f = hashlib.sha256()
    hash_f.update(msg.encode('utf-8'))
    return int(str(int(hash_f.hexdigest(), 16))[:HASH_LEN])

'''
Decrypt a message with a key, with the signature verification
If the signature is wrong, the function raise an exception
@param key : the key to decrypt
@param msg : the message to decrypt
@return : the key who was encrypted in the message
'''
def verify_signature(key:tuple, msg:list)->tuple:
    decrypt_message = decrypt(key,msg)
    receive_signature = decrypt_message[len(decrypt_message)-HASH_LEN:]
    receive_message = decrypt_message[:-HASH_LEN]
    key_receive = utils.msg2pb_key(receive_message)
    # Verify the footprint
    #decrypt signature
    decrypt_signature = decrypt(key_receive, receive_signature)
    # hash the message
    mess_hash = utils.int2lst(int(hash_mess(''.join(str(receive_message)))))
    # verification / test
    assert decrypt_signature == mess_hash, "Hash message is not the footprint"
    print("-- message not modify, signature OK --")
    return key_receive

'''
Take a key to send, with a footprint
@param key_send : the key to send
@param key_sig : the key to use to crypt the signature
@param key_crypt : the key to crypt the whole message
@return : the crypt message with the signature
'''
def send_key(key_send:tuple, key_sig:tuple, key_crypt:tuple)->list:
    message = utils.create_message(key_send)
    signature = crypt(key_sig, utils.int2lst(hash_mess(''.join(str(message)))))
    message_sign = message+signature
    to_send = crypt(key_crypt, message_sign)
    return to_send

'''
Main function
'''
def __main__():
    print(f"{'-'*10}Generating keys{'-'*10}")
    pb_A, pv_A = kg.generate_keys() # Alice keys
    pb_CA, pv_CA = kg.generate_keys() # CA keys
    while pb_A[1] > pb_CA[1]:
        pb_CA, pv_CA = kg.generate_keys()
    print(f"Alice :\n   public : {pb_A}\n   private : {pv_A}\n")
    print(f"Certificat center :\n   public : {pb_CA}\n   private : {pv_CA}\n")
    print(f"{'-'*10}Alice side{'-'*10}")
    alice_message = send_key(pb_A, pv_A, pb_CA)
    print(f"Alice crypt mess = {alice_message}\n")

    print(f"{'-'*10}CA side{'-'*10}")
    receive_key = verify_signature(pv_CA, alice_message)
    print(f'key receive : {receive_key}')
    message = utils.create_message(receive_key)
    CA_message = crypt(pv_CA, message)
    print(f"CA crypt message = {CA_message}\n")

    print(f"{'-'*10}Bob side{'-'*10}")
    decrypt_message = decrypt(pb_CA, CA_message)
    Alice_key = utils.msg2pb_key(decrypt_message)
    assert Alice_key == pb_A, "-- Bob receive the wrong key --"
    print('-- Bob receive the message --')
    print(f"Bob receive : {Alice_key}")


__main__()

"""
naive approch of is prime ( not used in this code )

def naive_is_prime(n: int)->bool:
    if n <= 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
"""
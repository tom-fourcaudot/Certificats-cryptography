import hashlib
import utils
import keygen as kg

HASH_LEN = 4

def crypt(key, mess):
    e, n = key
    res = []
    for c in mess:
        tmp = pow(int(c), e, n)
        res.append(tmp)
    return res

def decrypt(key, mess):
    d, n = key
    res = []
    for c in mess:
        tmp = pow(c, d, n)
        res.append(tmp)
    return res

def hash_mess(mess:str)->int:
    hash_f = hashlib.sha256()
    hash_f.update(mess.encode('utf-8'))
    return int(str(int(hash_f.hexdigest(), 16))[:HASH_LEN])

def verify_signature(pv_key, msg):
    decrypt_message = decrypt(pv_key,msg)
    receive_signature = decrypt_message[len(decrypt_message)-HASH_LEN:]
    receive_message = decrypt_message[:-HASH_LEN]
    key_receive = utils.msg2pb_key(receive_message)
    # On verifie la signature
    #decrypt signature
    decrypt_signature = decrypt(key_receive, receive_signature)
    # hash du message
    mess_hash = utils.int2lst(int(hash_mess(''.join(str(receive_message)))))
    # On verifie
    assert decrypt_signature == mess_hash, "Hash message is not the footprint"
    print("-- message not modify, signature OK --")
    return key_receive

def send_key(key_send, key_sig, key_crypt):
    message = utils.create_message(key_send)
    signature = crypt(key_sig, utils.int2lst(hash_mess(''.join(str(message)))))
    message_sign = message+signature
    to_send = crypt(key_crypt, message_sign)
    return to_send

def __main__():
    pb_A, pv_A = kg.generate_keys()
    pb_CA, pv_CA = kg.generate_keys()
    while pb_A[1] > pb_CA[1]:
        pb_CA, pv_CA = kg.generate_keys()

    print(f"{'-'*10}Alice side{'-'*10}")
    alice_message = send_key(pb_A, pv_A, pb_CA)
    print(f"Alice crypt mess = {alice_message}")

    print(f"{'-'*10}CA side{'-'*10}")
    receive_key = verify_signature(pv_CA, alice_message)
    print(receive_key)
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
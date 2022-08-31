from .caesar import * 
from .utils import *
import itertools
from collections import defaultdict

MAX_KEYLENGTH = 20

base_keylen_proportions = [0.26858405, 0.15936355, 0.10731316, 0.07769914, 0.06053305,
       0.05064498, 0.03970286, 0.0334287 , 0.02881092, 0.02584952,
       0.02133213, 0.01897305, 0.01847111, 0.01370276, 0.01234754,
       0.01174522, 0.01224715, 0.01144406, 0.0089344 , 0.00973749,
       0.00913517]


def vignere_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    # BEGIN SOLUTION
    padded_key = pad_key(key, len(plaintext))
    
    encrypted = ""
    for i in range(len(plaintext)):
        encrypted += shift_letter(plaintext[i], char_to_num(padded_key[i]))
    return encrypted
    # END SOLUTION

def vignere_decrypt(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    padded_key = pad_key(key, len(ciphertext))
    
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted += shift_letter(ciphertext[i], -char_to_num(padded_key[i]))
    return decrypted

from codebreaking_at_cal.caesar import * 
from codebreaking_at_cal.utils import *
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
    # BEGIN SOLUTION
    padded_key = pad_key(key, len(ciphertext))
    
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted += shift_letter(ciphertext[i], -char_to_num(padded_key[i]))
    return decrypted
    # END SOLUTION

def find_repeated_substrings(text):
    
    text=clean_text(text)
        
    appearances = defaultdict(lambda: 0)
    
    for i in range(2,len(text)//2):
        
        counts = defaultdict(lambda:-1)
        
        for k in range(0, len(text), i):
            if (k+3 > len(text)):
                continue
                        
            snippet_three = text[k:k+3]
            snippet_four = text[k:k+4]


            if (counts[snippet_three] != -1):
                appearances[i] += 1
            
            if (counts[snippet_four] != -1 and k+4 < len(text)):
                appearances[i] += 1
            
            counts[snippet_three] = k
            counts[snippet_four] = k
    
    return appearances

def keylen_proportions_from_text(text):
    parsed = np.fromiter(find_repeated_substrings(text).values(), dtype=int)[:MAX_KEYLENGTH+1]
    return parsed/sum(parsed)

def find_diff_from_base(text):
    # BEGIN SOLUTION
    text_keylen_proportions = keylen_proportions_from_text(text)
    
    diffs = text_keylen_proportions - base_keylen_proportions
    
    return diffs
    #END SOLUTION

def find_best_divisor(nums, diffs): # TODO fix
    result = []
    k = 1
    for num in nums:
        score = 0

        for i in range(2*num, MAX_KEYLENGTH+3, num):
            if (diffs[i-num-2] < diffs[i - 2]):
                score -= 1
        k+=1
        
        result.append((num, score))
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return [x[0] for x in result[:3]]

def find_vignere_key_lengths(ciphertext):
    # BEGIN SOLUTION
    diffs = find_diff_from_base(ciphertext)    
    
    potential = []
    for i in range(2, MAX_KEYLENGTH+2):
        if diffs[i-2] > 0:
            potential.append(i)
    
    return find_best_divisor(potential, diffs)
    # END SOLUTION

def crack_vignere(ciphertext):
    keylengths = find_vignere_key_lengths(ciphertext)
    
    finalstrs = []
    
    for keylen in keylengths:
        # BEGIN SOLUTION
        texts = ['' for i in range(keylen)]
        
        k = 0
        for char in ciphertext:
            texts[k%keylen] += char
            k+=1
            
        cracked_texts = [crack_caesar(text) for text in texts]
        
        finalstr = ""
    
        for i in range(len(ciphertext)):
            finalstr += cracked_texts[i%keylen][i//keylen]
        
        finalstrs.append(finalstr)

        #END SOLUTION
    
    
    #BEGIN SOLUTION
    return min(finalstrs, key = lambda x: tvd(np_english_frequencies, calculate_proportions(x)))
    # END SOLUTION


from codebreaking_at_cal import * 

print(vignere_encrypt("hello there, how are you? I am good, thank you.", "hi"))
print(vignere_decrypt(vignere_encrypt("hello there, how are you? I am good, thank you.", "hi"), "hi"))
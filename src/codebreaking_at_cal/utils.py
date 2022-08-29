import re


def char_to_num(text):
    return ord(text.lower()) - 97

def num_to_char(num):
    return chr(num + 97).lower()

def clean_text(text):
    return re.sub('[^A-Za-z\s!?.,$]*', '', text.lower())

def tvd(freq1, freq2):
    # Takes in two numpy arrays of length 26.
    # BEGIN SOLUTION
    diff = abs(freq1 - freq2)
    return sum(diff)/2
    # END SOLUTION
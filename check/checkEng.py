"""Check English"""

def check_eng():
    """Check English"""
    text = input()
    alphabet_no_shift = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_shift = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
         'M', 'N', 'O', 'P' ,'Q' ,'R' ,'S' ,'T', 'U', 'V', 'W', 'X','Y', 'Z']
    for i in text:
        if i in alphabet_no_shift:
            print('ENG NO SHIFT')
        elif i in alphabet_shift:
            print('ENG SHIFT')
        else:
            print('OTHER LANGUAGES')

check_eng()

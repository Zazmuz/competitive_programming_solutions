alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}
alp = set(alp)
def is_palindrome(s):
    if s == "":
        return False
    return s == s[::-1]
def to_morse(s):
    return "".join([morse_dict[c] for c in s])

def remove_non_alp(s):
    return "".join([c for c in s if c in alp])

print(1 if is_palindrome(to_morse(remove_non_alp(input().upper()))) else 0)
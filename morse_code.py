#-------------------------------------------------------------------------------
# Name:        morse_code.py
# Purpose:
#
# Author:      Akshay
#
# Created:     12-06-2015
#-------------------------------------------------------------------------------

morse = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L':'._..', 'M':'__',
'N': '_.', 'O':'___', 'P':'.__.', 'Q': '__._', 'R':'._.', 'S':'...', 'T':'_',
'U': '.._', 'V': '..._', 'W':'.__', 'X': '_.._','Y': '_.__', 'Z':'__..'
}

reverse_morse = {}

def create_dict():
    p = morse.items()
    for k,v in p:
        reverse_morse[v] = k

create_dict()

def remove_puncts_and_upper(sentence):
    res = ''
    valid = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    valid += [chr(x) for x in range(ord('a'), ord('z') + 1)]
    valid.append(' ')
    valid.append('.')
    for c in sentence:
        if c in valid:
            res += str.upper(c)

    return res

def to_morse(sentence):
    """
    Convert a string sentence into equivalent morse code with words separated by newline, and sentences seperated by two new lines.
    Ignore non-alphabet characters excluding space and period.
    Case insensitive.
    """
    sentence = sentence.strip()
    if sentence[-1] != '.':
        sentence[-1] = '.'
    #sentence = sentence + ' '
    sentence = remove_puncts_and_upper(sentence)
    res = ''
    for c in sentence:
        if c in (' ', '.'):
            res = res + ' ' + '\n'
        else:
            res = res + morse[c] + '\n'
    return res

def valid_morse(encoded):
    """Return whether encoded is valid morse coded string."""
    temp = encoded.split('\n')
    temp = [x for x in temp if x]
    v = list(reverse_morse.keys())
    v.append(' ')
    for s in temp:
        if s not in v:
            return False

    return True

def to_plain_text(encoded):
    """Decode morse coded string."""
    assert valid_morse(encoded), "Cannot decode this invalid morse code."
    res = ''
    temp = encoded.split('\n')
    temp = [x for x in temp if x]
    #print(temp)
    for i, letter in enumerate(temp):
        if letter == ' ':
            try:
                if temp[i+1] == ' ':
                    res += '.'
                else:
                    res += ' '
            except IndexError:
                res += '.'
        else:
            c = reverse_morse[letter]
            res += c
    return res

def valid(s):
    valid = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    valid += [chr(x) for x in range(ord('a'), ord('z') + 1)]
    valid.append(' ')
    valid.append('.')
    for c in s:
        if c not in valid:
            return False

    return True

def get_input(msg):
    inp = None
    while True:
        inp = input(msg)
        if valid(inp):
            break
        else:
            print('Cannot convert this string to morse due to special characters. Only A-Z, period, and space characters allowed.')

    return inp


def main():
    text = get_input('Enter a string to be converted to morse code.')
    print('The encoded string is:\n{}'.format(to_morse(text)))

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
# Name:        word_game
# Purpose:
#
# Author:      Akshay
#
# Created:     16-06-2015
#-------------------------------------------------------------------------------

import random


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
WORDS_FILE_PATH = 'F:\Python\Python-mini-projects\words.txt'
HAND_SIZE = 10

def load_words():
    """Load words from file at path WORDS_FILE_PATH and return list of words."""
    words = []
    print('Loading words...')
    with open(WORDS_FILE_PATH,'r', encoding='utf-8') as words_file:
        for word in words_file:
            words.append(word.strip().lower())

    print('%d words loaded.' %len(words))
    return words

def deal_hand(n):
    """Deal a hand of n letters where at least 30% are vowels."""
    hand = []
    for i in range(n//3):
        hand.append(random.choice(VOWELS))

    i += 1
    while i < n:
        i += 1
        hand.append(random.choice(CONSONANTS))

    #random.shuffle(hand)
    return get_frequency_dict(hand)

def get_word_score(word, hand_size):
    """
    Score of a word = sum of scrabble scores*len(word) + 50 if all letters used.
    Preconditions: word -> string (lowercase)
                   hand_size -> int

    Postcondition: return an int >= 0
    """

    ans = 0
    for c in word:

        ans += SCRABBLE_LETTER_VALUES[c]

    ans = ans*len(word)

    if len(word) == hand_size:
        ans += 50
    return ans

def get_frequency_dict(list_of_chars):
    res = {}
    for c in list_of_chars:
        res[c] = res.get(c,0) + 1

    return res

def display_hand(hand):

    for e in hand.keys():
        for i in range(hand[e]):
            print(e, end = ' ')

    print()

def update_hand(h, word):
    import copy
    hand = copy.deepcopy(h)

    for c in word:
        hand[c] -= 1
        if not hand[c]:
            _ = hand.pop(c,None)

    return hand

def is_valid_word(word, hand, word_list):
    if word not in word_list:
        return False

    word_freq = get_frequency_dict(word)
    for e in word_freq:
        try:
            if hand[e] < word_freq[e]:
                return False
        except KeyError:
            return False
    return True

def hand_len(hand):
    return sum(hand.values())

def play_hand(hand, word_list = load_words()):
    score = 0
    while hand:
        print('Current Hand: ', end='')
        display_hand(hand)
        word = input('Enter word, or a "." to indicate that you are finished:')
        if word == '.':
            break
        if not is_valid_word(word, hand, word_list):
            print('Invalid word, please try again.')

        else:
            word_score = get_word_score(word, HAND_SIZE)
            score += word_score
            print('%s earned %d points. Total: %d points' %(word, word_score, score))


            hand = update_hand(hand, word)


    if not hand:
        print('Run out of letters.', end = ' ')
    else:
        print('Goodbye!', end = ' ')
    print('Total score: %d points' %score)


def play_game(word_list):
    prev_hand = None
    hand = None

    while True:
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand)
            prev_hand = hand
        elif choice == 'r':
            if prev_hand is not None:
                hand = prev_hand
                play_hand(hand,word_list)
            else:
                print('You have not played a hand yet. Please play a new hand first!')
        elif choice == 'e':
            break
        else:
            print('Invalid command.')


def compChooseWord(hand, wordList, n = HAND_SIZE):
    best = 0
    best_word = ''
    for word in wordList:
        if is_valid_word(word, hand, wordList):
            s = get_word_score(word,n)
            if s > best:
                best = s
                best_word = word


    return best_word

def compPlayHand(hand, wordList = load_words()[:1000], n = HAND_SIZE):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    while hand_len(hand):
        print('Current Hand: ', end='')
        display_hand(hand)
        word = compChooseWord(hand,wordList, n)
        if word is not None:
            word_score = get_word_score(word,n)
            score += word_score
            print('\"%s\" earned %d points. Total: %d points' %(word, word_score, score))
        else:
            break
        hand = update_hand(hand, word)

def playGame(wordList):
    prev_hand = None
    hand = None

    while True:
        flag = False
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'n':
            hand = deal_hand(HAND_SIZE)
            flag = True
        elif choice == 'r':
            if prev_hand is not None:
                hand = prev_hand

                Flag = True
            else:
                print('You have not played a hand yet. Please play a new hand first!')
        elif choice == 'e':
            break
        else:
            print('Invalid command.')

        if flag:
            while True:
                user = input('Enter u to have yourself play, c to have the computer play:')
                if user == 'u':
                    play_hand(hand, wordList)
                    break
                elif user == 'c':
                    compPlayHand(hand, wordList)
                    break
                else:
                    print('Invalid command.')

            prev_hand = hand


def main():
    #words = load_words()
    #play_game(words)
    pass

if __name__ == '__main__':
    main()








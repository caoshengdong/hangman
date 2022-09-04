import re


def guess_next_letter(pattern, used_letters=[], word_list=['about', 'abound']):
    """Returns a letter from the alphabet.
    Input parameters:
        pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
    length = len(pattern)
    regex_pattern = pattern.replace('_', r'\w')

    word_list = list(filter(lambda x: (len(x) == length), word_list))
    word_list = list(filter(lambda x: (re.match(regex_pattern, x)), word_list))

    # collect all letters from word_list
    letters_count = {}
    for word in word_list:
        for letter in word:
            letters_count[letter] = letters_count.get(letter, 0) + 1

    # sort letters_count by value desc
    letters_count = sorted(letters_count.items(), key=lambda x: x[1], reverse=True)
    # get first letter from letters_count that is not in used_letters
    for letter, count in letters_count:
        if letter not in used_letters:
            return letter


if __name__ == '__main__':
    actual = 'word'
    result = '____'
    used_letters_ = []

    # read words from file
    with open('words.txt', 'r') as f:
        word_list = f.read().splitlines()

    while result != actual:
        guessed_letter = guess_next_letter(result, used_letters=used_letters_, word_list=word_list)
        print('guessed letter', guessed_letter)
        if guessed_letter in actual:
            # replace _ to actual letter
            result = ''.join([actual[i] if actual[i] == guessed_letter else result[i] for i in range(len(actual))])
        used_letters_.append(guessed_letter)
        print(result)

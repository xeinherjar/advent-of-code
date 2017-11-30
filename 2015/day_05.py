def run():
    nice = 0
    nice_new_rules = 0
    with open('day_05_input', 'r') as f:
        for line in f:
            if rule1(line) and rule2(line) and rule3(line):
                nice = nice + 1
            if rule4(line) and rule5(line):
                nice_new_rules = nice_new_rules + 1

    print('Total lines that are nice', nice)
    print('Total lines that are nice (new rules)', nice_new_rules)

def rule1(text):
    """ Vowels must appear at least 3 times, set of { aeiou } """
    vowels = set('aeiou')
    count = 0
    for letter in text:
        if letter in vowels:
            count = count + 1

    return count >= 3

def rule2(text):
    """ A letter must appear twice in a row, aa, bb, cc etc """
    for idx in range(len(text) -2):
        if text[idx] == text[idx + 1]:
            return True
    return False

def rule3(text):
    """ Must NOT contain ab, cd, pq, or xy """
    if any(sub in text for sub in ['ab', 'cd', 'pq', 'xy']):
        return False
    return True


def rule4(text):
    """ two letters must appear twice next to each other with no overlap, ie
    xf should appear twice, xfxf would be okay, abaab is okay, aaab is not as a
    overlapse """
    for idx in range(len(text) -2):
        if text[idx:idx+2] in text[idx+2:]:
            return True
    return False


def rule5(text):
    """ Must have letter repeat one character away, ie fxf, ddd, aba """
    for idx in range(len(text) -3):
        if text[idx] == text[idx + 2]:
            return True
    return False



if __name__ == '__main__':
    run()

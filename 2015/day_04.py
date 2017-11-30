import hashlib

def run():
    secret_input = b'iwrupvqb'
    counter = 0

    guess = ''

    while guess[:6] != '000000':
        counter = counter + 1
        guess = secret_input + str(counter).encode()
        md5 = hashlib.md5(guess)
        guess = md5.hexdigest()


    print(guess[:6], guess, counter)






if __name__ == '__main__':
    run()

i = 0
n = ['black', 'white', 'black', 'white', 'black', 'white', 'white', 'white', 'black', 'black']
answers = []
success_min = len(n) - 1

def find_parity(known):

    print "known: " + str(known)
    no_white = known.count('white')
    print "number of white hats: " + str(no_white)
    if no_white % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    # parity = 'odd'
    print "parity: " + parity
    return parity

def my_hat(n, i, success_min):
    incorrect = 0
    correct = 0
    while i < len(n):
        # riddle logic
        known = n[i+1:]
        known_parity = find_parity(known)
        if i == 0:
            if known_parity == 'even':
                guess = 'white'
            else:
                guess = 'black'
        elif i == 1:
            if current_parity != known_parity:
                print "current_parity != known_parity"
                if guess == 'white':
                    guess = 'black'
                else:
                    guess = 'white'
            else:
                print "current_parity == known_parity"
        else:
            past = answers[1:]
            print "past: " + str(past)
            new_known = past + known
            print "new_known: " + str(new_known)
            last = answers[-1]
            print "last: " + last

            known_parity = find_parity(new_known)
            if current_parity != known_parity:
                print "current_parity != known_parity"
                if last == 'white':
                    guess = 'black'
                else:
                    guess = 'white'
            else:
                print "current_parity == known_parity"

        current_parity = known_parity
        answers.append(guess)
        print "guess: " + guess
        print "answers: " + str(answers)

        # riddle logic
        if guess == n[i]:
            correct += 1
            print "correct: " + str(correct)
        else:
            incorrect += 1
            print "incorrect" + str(incorrect)
        i += 1
    print "minimum needed to succeed: " + str(success_min)
    return correct >= success_min

print "Passed? " + str(my_hat(n, i, success_min))

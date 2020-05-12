from random import sample, shuffle
from re import sub as re_replace, search

### Customization Constants
NUMBER_OF_COLORS = 8 #max-colors = 9
CODE_SIZE = 4        #max-size   = 9
MAX_GUESSES = 10

if __name__ == '__main__':
    ### Game Setup
    colors = list(range(1, NUMBER_OF_COLORS + 1))
    invalid_colors = list(set(range(10)).difference(colors))
    regex = str(invalid_colors).replace(', ','')

    ### Code generation
    print('Generating code...')
    code = sample(colors,CODE_SIZE)
    code_broken = False
    print('Code generated!\n')

    ### Game Core
    for k_guess in range(MAX_GUESSES):
        ### Guess entry
        guess = input(f'Guess #{k_guess + 1}: ')
        guess = re_replace(r'\D','',guess)

        ### Guess validation
        while len(guess) is not CODE_SIZE or search(regex,guess):
            print(f'The guess must have exactly {CODE_SIZE} digits between 1~{NUMBER_OF_COLORS}\n')

            guess = input(f'Guess #{k_guess + 1}: ')
            guess = re_replace(r'\D','',guess)

        ### Get feedback
        guess = list(map(int, guess))
        feedback = []
        for (index,color) in enumerate(guess):
            if color in code:
                feedback.append('black' if code[index] is color else 'white')

        ### Show the feedback
        shuffle(feedback)
        print(feedback,'\n')

        ### Verify game over
        if guess == code:
            code_broken = True
            break

    ### Final message
    if code_broken:
        print('Good job! You broke the code.')
    else:
        print(f'The code was {code}. Better luck next time.')
    input('(Press enter to exit)')

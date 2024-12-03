x = 123

def hello(name):
    return f'Hello, {name} from menu'

def menu(options):
    while True:
        choice = input(f'Enter your choice ({options}): ').strip()

        if choice in options:
            return choice

        print(f'Bad option; try again')

if __name__ == '__main__':
    print('Demoing the menu function...')

    user_choice = menu(['a', 'b', 'c'])
    print(f'You chose {user_choice}')
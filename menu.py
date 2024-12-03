x = 123

def hello(name):
    return f'Hello, {name} from menu'

def menu(options):
    while True:
        choice = input('Enter your choice: ').strip()

        if choice in options:
            return choice

        print(f'Bad option; try again')
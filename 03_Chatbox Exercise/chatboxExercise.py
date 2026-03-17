botName: str = 'Ace'
print(f'Hello, my name is {botName}!, how can I help you?: ')

while True:
    userName: str = input('You: ').lower()

    if userName in ['hi', 'hello']:
        print(f'{botName}: Hello there')
    elif userName in ['bye', 'goodbye', 'see you']:
        print(f'{botName}: Goodbye!')
        break
    elif userName in ['+', 'add', 'plus']:
        print(f"{botName}: Sure, let's do some addition, enter 2 numbers")
        try:
            num1: int = int(input('Enter first number: '))
            num2: int = int(input('Enter second number: '))
            print(f'{botName}: The sum of the two numbers are {num1 + num2}')
        except ValueError:
            print(f'{botName}: Sorry, please enter a valid number: ')
    else:
        print(f"{botName}: I'm sorry, I do not understand that, please try again")

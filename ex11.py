name = input(f"What's your name? ")
years = int(input(f"How old are you? "))
birthday = input(f'Whens your birthday? ')
def greetings():
    print(f'{name} is {years} years old and is turning {years + 1} on {birthday}')
greetings()

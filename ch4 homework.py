# Chase Stern Chapter 4 Homework

# Variable for yes
decision = 'y'

# Make a loop
while decision == 'y' or decision == 'Y':
    # Homework title
    print(f'Where do you belong in school?')

    # Input for age
    age = int(input(f'Please enter your age: '))

    # Looping for invalid numbers
    if age < 0 or age > 100:
        print(f'Please enter a valid number.')
        continue # Loops program if you enter a negative number or >100
    
    # If/else statements for age
    if age >= 0 and age <= 5:
        print(f'You are too young for elementary school.')

    elif age >= 6 and age <= 10:
        print(f'You are in Elementary School.')

    elif age >= 11 and age <= 13:
        print(f'You are in Middle School.')

    elif age >= 14 and age <= 18:
        print(f'You are in High School')

    elif age >= 19:
        print(f"You're an adult. Choose your career path.")

        
    # Try again
    decision = input('Enter another age? (y/n): ')

    # Goodbye message for no decision
    if decision == 'n' or decision == 'N':
        print('Thank you for using this program. Goodbye')

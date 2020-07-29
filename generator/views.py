from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    # Using list() to create lists of characters from strings
    lowercases = list('abcdefghijklmnopqrstuvwxyz')
    uppercases = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    specials = list('!"£$%^&*()_-+={[}];:@#~,<.>/?|')
    # We will always quarantee lower case letters
    choices = ['lower']
    # Get the length value from the query string and also set default value of 10 in case no query string
    length = int(request.GET.get('length', 10))
    # Basic error check for minimum password length of 6
    if length < 6:
        length = 6
    # Check for selected options
    if request.GET.get('uppercase'):
        choices.append('upper')
    if request.GET.get('numbers'):
        choices.append('number')
    if request.GET.get('specials'):
        choices.append('special')
    # Start with empty password
    generated_password = ''
    # Define empty list for keeping score of choices used 
    usedchoices = []
    # Loop through entire length and make sure we get at least one of everything
    # TODO - Here some logic should be added to ensure all choices are used at least once
    for x in range(length):
        # Get a random type of characters (lowercase, uppercase, etc)
        current_choice = random.choice(choices)
        # Check if this is a new choice or if it has been used before
        if current_choice in usedchoices:
            pass
        else:
            usedchoices.append(current_choice)
        if current_choice == 'lower':
            generated_password += random.choice(lowercases)
        elif current_choice == 'upper':
            generated_password += random.choice(uppercases)
        elif current_choice == 'number':
            generated_password += random.choice(numbers)
        elif current_choice == 'special':
            generated_password += random.choice(specials)        

    # Sort the two choices lists
    choices.sort()
    usedchoices.sort()
    # Compare the two lists and give user feedback in case they do not contain the same elements
    if choices == usedchoices:
        message = 'Successfully generated the password with all your choices applied'
        alertlevel = 'success'
    else:
        message = 'Failed to include all your choices - use with care or generate a new password'
        alertlevel = 'error'

    return render(request, 'generator/password.html', {'password': generated_password, 'message': message, 'alertlevel': alertlevel})
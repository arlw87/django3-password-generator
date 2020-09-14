from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    length = int(request.GET.get('passwordLength'))
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    punc = string.punctuation

    characters_to_select = letters_lower

    if "Uppercase" in request.GET:
        characters_to_select = characters_to_select + letters_upper
    if "numbers" in request.GET:
        characters_to_select = characters_to_select + digits
    if "specialCharacters" in request.GET:
        characters_to_select = characters_to_select + punc

    newPassword = ''
    for i in range(0, length):
        newPassword = newPassword + random.choice(characters_to_select)

    #generate a random password
    thepassword = newPassword

    return render(request, 'generator/password.html', {'password': thepassword})

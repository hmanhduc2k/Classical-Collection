from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from ..models import User, Favorite
from classcoll.utils import PasswordStrength

LOGIN_FILE = "classcoll/login.html"
REGISTER_FILE = "classcoll/register.html"

MESSAGE_INVALID_CREDENTIALS = "Invalid username and/or password."
MESSAGE_USERNAME_EXISTED = "Username already taken."
MESSAGE_PASSWORD_MATCH = "Invalid Registration: Passwords must match!"
MESSAGE_PASSWORD_LENGTH = "Invalid Registration: Passwords must contain at least 8 characters!"
MESSAGE_PASSWORD_SIMILARITY = "Invalid Registration: Passwords must not be similar to username!"
MESSAGE_PASSWORD_COMPLEXITY = "Invalid Registration: Passwords must contain at least an alphanumeric and a special character!"

def loginPage(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, LOGIN_FILE, {
                "message": MESSAGE_INVALID_CREDENTIALS
            })
    else:
        return render(request, LOGIN_FILE)


def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def registerPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        
        message = ""
        proceeded = True
        if password != confirmation:
            proceeded = False
            message = MESSAGE_PASSWORD_MATCH  
        elif not PasswordStrength.minLength(password):
            proceeded = False
            message = MESSAGE_PASSWORD_LENGTH
        elif not PasswordStrength.minDifference(username, password):
            proceeded = False
            message = MESSAGE_PASSWORD_SIMILARITY
        elif not PasswordStrength.minComplex(password):
            proceeded = False
            message = MESSAGE_PASSWORD_COMPLEXITY
        
        if not proceeded:
            return render(request, REGISTER_FILE, {
                "message": message
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            favorite = Favorite.objects.create(user=user)
            favorite.save()
        except IntegrityError:
            return render(request, REGISTER_FILE, {
                "message": MESSAGE_USERNAME_EXISTED
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, REGISTER_FILE)
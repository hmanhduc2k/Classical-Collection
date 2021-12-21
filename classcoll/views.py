from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.files.storage import FileSystemStorage

from .models import *

fs = FileSystemStorage()

# Create your views here.
def index(request):
    return render(request, 'classcoll/index.html')


def login_view(request):
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
            return render(request, "classcoll/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "classcoll/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "classcoll/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "classcoll/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "classcoll/register.html")
    
def allPieces(request):
    if request.method == 'POST':
        name = request.POST['name']
        composer = request.POST['composer']
        description = request.POST['description']
        uploadedFile = request.FILES['document']
        newPiece = Piece(
            name = name,
            composer = composer,
            description = description,
            source = uploadedFile
        )
        newPiece.save()
        fs.save(uploadedFile.name, uploadedFile)
        return render(request, 'classcoll/piece.html', {
            'uploaded': True,
            'source': uploadedFile
        })
    return render(request, 'classcoll/all_pieces.html', {
        'uploaded': False
    })
    
def allComposers(request):
    if request.method == 'POST':
        name = request.POST['name']
        biography = request.POST['biography']
        image = request.FILE['document']
        fs.save(image.name, image)
        newComposer = Composer(
            name=name,
            biography=biography,
            image=image
        )
        newComposer.save()
        return redirect('index')
    return render(request, "classcoll/all_composer.html", {
        'composers': Composer.objects.all()
    })

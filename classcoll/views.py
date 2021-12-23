import json
from django.http.response import JsonResponse

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
        composerName = request.POST['composer']
        composer = Composer.objects.filter(name=composerName).first()
        description = request.POST['description']
        uploadedFile = request.FILES['document']
        period = Period.objects.filter(era=request.POST['period']).first()
        difficulty = Difficulty.objects.filter(rating=request.POST['difficulty']).first()
        newPiece = Piece(
            name = name,
            composer = composer,
            description = description,
            source = uploadedFile,
            period = period,
            difficulty = difficulty
        )
        newPiece.save()
        fs.save(uploadedFile.name, uploadedFile)
        return redirect('index')
    else:
        return render(request, 'classcoll/all_pieces.html', {
            'periods': Period.objects.all(),
            'difficulty': Difficulty.objects.all(),
            'pieces': Piece.objects.all()
        })
    
def allComposers(request):
    if request.method == 'POST':
        name = request.POST['name']
        biography = request.POST['biography']
        image = request.POST['document']
        newComposer = Composer(
            name=name,
            biography=biography,
            image=image
        )
        newComposer.save()
        return redirect('index')
    else:
        return render(request, "classcoll/all_composers.html", {
            'composers': Composer.objects.all()
        })

def composer(request, name):
    try:
        target = Composer.objects.filter(name=name).first()
    except:
        redirect('index')
    pieces = Piece.objects.filter(composer=target)
    return render(request, "classcoll/composer.html", {
        'composer': target,
        'pieces': pieces
    })
    
def piece(request, name):
    try:
        target = Piece.objects.filter(name=name).first()
    except:
        redirect('index')
    return render(request, 'classcoll/piece.html', {
        'piece': target
    })

def comment(request, id):
    if request.method == 'POST':
        piece = Piece.objects.filter(id=id).first()
        data = json.loads(request.body)
        return JsonResponse(status=200)
    # elif request.method == 'PUT':
    # elif request.method == 'DELETE'
    else:
        return JsonResponse(status=404)
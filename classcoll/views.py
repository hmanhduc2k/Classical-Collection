import json
from django.db.models.fields import NullBooleanField
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Count
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
            favorite = Favorite.objects.create(user=user)
            favorite.save()
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
        # fs.save(uploadedFile.name, uploadedFile)
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

@login_required(login_url='login')
def composer(request, name):
    try:
        target = Composer.objects.filter(name=name).first()
    except:
        redirect('index')
    pieces = Piece.objects.filter(composer=target)
    favorite = Favorite.objects.filter(user=request.user).first().composers.all()
    return render(request, "classcoll/composer.html", {
        'composer': target,
        'pieces': pieces,
        'favorite': favorite
    })

@csrf_exempt
def favcomposer(request, id):
    try:
        target = Composer.objects.filter(pk=id).first()
        print(target)
    except:
        redirect('index')
    if request.method == 'PUT':
        fav = Favorite.objects.filter(user=request.user).first()
        if target in fav.composers.all():
            fav.composers.remove(target)
            fav.save()
            return JsonResponse({"message": "Add to Favorite"}, status=200)
        else:
            fav.composers.add(target)
            fav.save()
            return JsonResponse({"message": "Remove from Favorite"}, status = 200)
        
@csrf_exempt
def favpiece(request, id):
    try:
        target = Piece.objects.filter(pk=id).first()
        print(target)
    except:
        redirect('index')
    if request.method == 'PUT':
        fav = Favorite.objects.filter(user=request.user).first()
        if target in fav.pieces.all():
            fav.pieces.remove(target)
            fav.save()
            return JsonResponse({'message': 'Add to Favorite'}, status=200)
        else:
            fav.pieces.add(target)
            fav.save()
            return JsonResponse({'message': 'Remove from Favorite'}, status=200)
    
def piece(request, name):
    try:
        target = Piece.objects.filter(name=name).first()
    except:
        redirect('index')
    comments = Comment.objects.filter(piece=target).annotate(upvotes=Count('upvote')).order_by('-time')
    temp = Upvote.objects.filter(user=request.user)
    upvotes = []        # get a list of all upvoted comments by the users
    for upvote in temp:
        if upvote.comment in comments:
            upvotes.append(upvote.comment)
    favorite = Favorite.objects.filter(user=request.user).first().pieces.all()
    
    return render(request, 'classcoll/piece.html', {
        'piece': target,
        'comments': comments,
        'upvotes': upvotes,
        'favorite': favorite
    })
    
def favorite(request):
    user = request.user
    fav = Favorite.objects.filter(user=user).first()
    pieces = fav.pieces.all()
    composers = fav.composers.all()
    return render(request, 'classcoll/favorite.html', {
        'pieces': pieces,
        'composers': composers
    })

@csrf_exempt
def comment(request, id):
    print('Hello World')
    if request.method == 'POST':
        data = json.loads(request.body)
        # id refers to piece id
        target = Piece.objects.filter(id=id).first()
        newComment = Comment.objects.create(
            user=request.user,
            content=data.get('content'),
            piece=target
        )
        newComment.save()
        return JsonResponse(status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        existedComment = Comment.objects.filter(
            id = id,
            user = request.user,
        ).first()
        existedComment.content = data.get('content')
        existedComment.save()
        return JsonResponse(status = 200)
    elif request.method == 'DELETE':
        existedComment = Comment.objects.filter(
            pk = id
        ).first()
        existedComment.delete()
        return JsonResponse({'message': 'success'}, status = 200)

@csrf_exempt
def upvote(request, id):
    if request.method == 'PUT':
        comment = Comment.objects.filter(id = id).first()
        upvoted = Upvote.objects.filter(
            user = request.user,
            comment = comment
        ).first()
        if upvoted is not None:
            upvoted.delete()
            return JsonResponse({'status': False}, status = 200)
        else:
            upvoted = Upvote.objects.create(
                user = request.user,
                comment = comment
            )
            upvoted.save()
            return JsonResponse({'status': True}, status = 200)
        
def sort(request, type):
    if type == 'period':
        return None
    elif type == 'difficulty':
        return None
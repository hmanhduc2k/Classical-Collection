from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import Favorite, Composer, Piece

@login_required(login_url='login')
@csrf_exempt
def favoriteComposer(request, id):
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

@login_required(login_url='login')
@csrf_exempt
def favoritePiece(request, id):
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

@login_required(login_url='login')
def userFavorite(request):
    user = request.user
    fav = Favorite.objects.filter(user=user).first()
    pieces = fav.pieces.all()
    composers = fav.composers.all()
    return render(request, 'classcoll/favorite.html', {
        'pieces': pieces,
        'composers': composers
    })
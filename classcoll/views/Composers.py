from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from ..models import Composer, Piece, Favorite
   
COMPOSER_LIST_FILE = "classcoll/all_composers.html"
COMPOSER_FILE = "classcoll/composer.html"
ERROR_FILE = 'classcoll/error.html'

MESSAGE_COMPOSER_EXISTED = 'Composer has already existed!'

def allComposers(request):
    if request.method == 'POST':
        name = request.POST['name']
        biography = request.POST['biography']
        image = request.POST['document']
        
        if Composer.objects.filter(name=name).first() is not None:
            return render(request, COMPOSER_LIST_FILE, {
                'composers': Composer.objects.all(),
                'message': MESSAGE_COMPOSER_EXISTED
            })
        newComposer = Composer(
            name=name,
            biography=biography,
            image=image
        )
        newComposer.save()
        return redirect('index')
    else:
        key = request.GET.get("key", "")
        composers = []
        for composer in Composer.objects.all():
            if key in composer.name:
                composers.append(composer)
                
        paginator = Paginator(composers, 5)
        pageNumber = request.GET.get('page')
        composers = paginator.get_page(pageNumber)
        return render(request, COMPOSER_LIST_FILE, {
            'composers': composers
        })

def composerInfo(request, name):
    try:
        target = Composer.objects.filter(name=name).first()
    except:
        render(request, ERROR_FILE)
    pieces = Piece.objects.filter(composer=target)
    favorite = []
    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(user=request.user).first().composers.all()
    return render(request, COMPOSER_FILE, {
        'composer': target,
        'pieces': pieces,
        'favorite': favorite
    })
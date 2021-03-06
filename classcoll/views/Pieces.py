from django.shortcuts import render, redirect
from django.db.models import Count
from django.core.paginator import Paginator

from ..models import *
from classcoll.utils import ComposerSearch, PieceSearch

KEYWORD_ALL = "All"

ALL_PIECE_FILE = 'classcoll/all_pieces.html'
PIECE_FILE = 'classcoll/piece.html'
ERROR_FILE = 'classcoll/error.html'

MESSAGE_COMPOSER_NOT_FOUND = 'No composer found. Make sure that the name is exactly as it is.'
 
def allPieces(request):
    if request.method == 'POST':
        name = request.POST['name']
        composerName = request.POST['composer']
        composer = ComposerSearch.search(composerName)
        if composer is None:
            return render(request, ALL_PIECE_FILE, {
            'periods': Period.objects.all(),
                'difficulty': Difficulty.objects.all(),
                'pieces': Piece.objects.all(),
                'message': MESSAGE_COMPOSER_NOT_FOUND
            })
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
        return redirect('index')
    else:
        key = request.GET.get("key", "")
        pr = request.GET.get("period", KEYWORD_ALL)
        df = request.GET.get("difficulty", KEYWORD_ALL)
        pieces = []
        for piece in Piece.objects.all():
            if PieceSearch.match(piece, key, pr, df):
                pieces.append(piece)

        paginator = Paginator(pieces, 5)
        pageNumber = request.GET.get('page')
        pieces = paginator.get_page(pageNumber)
        return render(request, ALL_PIECE_FILE, {
            'periods': Period.objects.all(),
            'difficulty': Difficulty.objects.all(),
            'pieces': pieces
        })
        
def pieceInfo(request, name):
    target = Piece.objects.filter(name=name).first()
    if target is None:
        return render(request, ERROR_FILE)
    comments = Comment.objects.filter(piece=target).annotate(upvotes=Count('upvote')).order_by('-upvote')
    temp = Upvote.objects.filter(user=request.user)
    upvotes = []        # get a list of all upvoted comments by the users
    for upvote in temp:
        if upvote.comment in comments:
            upvotes.append(upvote.comment)
    favorite = []
    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(user=request.user).first().pieces.all()
    paginator = Paginator(comments, 10)
    pageNumber = request.GET.get('page')
    comments = paginator.get_page(pageNumber)
    
    return render(request, PIECE_FILE, {
        'piece': target,
        'comments': comments,
        'upvotes': upvotes,
        'favorite': favorite
    })
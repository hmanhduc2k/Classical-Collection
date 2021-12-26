import random
from django.shortcuts import render

from ..models import Composer, Piece

INDEX_FILE = 'classcoll/index.html'

def homePage(request):
    composers = Composer.objects.all()
    pieces = Piece.objects.all()
    randomComposer = random.choice(composers)
    randomPiece = random.choice(pieces)
    return render(request, INDEX_FILE, {
        'composer': randomComposer,
        'piece': randomPiece
    })
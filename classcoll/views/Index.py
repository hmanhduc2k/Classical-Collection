import random
from django.shortcuts import render

from ..models import Composer, Piece

def landingPage(request):
    composers = Composer.objects.all()
    pieces = Piece.objects.all()
    randomComposer = random.choice(composers)
    randomPiece = random.choice(pieces)
    return render(request, 'classcoll/index.html', {
        'composer': randomComposer,
        'piece': randomPiece
    })
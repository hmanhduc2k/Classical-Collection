import difflib

from ..models import Composer

COMPOSERS = Composer.objects.all()
THRESHOLD = 0.8

def search(input):
    for composer in COMPOSERS:
        if difflib.SequenceMatcher(None, composer.name, input).ratio() >= THRESHOLD:
            return composer
    return None
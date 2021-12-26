from django.shortcuts import render

from ..models import Period, Difficulty

ERROR_FILE = 'classcoll/error.html'
PERIOD_FILE = 'classcoll/period.html'
DIFFICULTY_FILE = 'classcoll/difficulty.html'

def period(request, name):
    target = Period.objects.filter(era=name).first()
    if target is None:
        return render(request, ERROR_FILE)
    else:
        return render(request, PERIOD_FILE, {
            'periods': Period.objects.all(),
            'target': target
        })
    
def difficulty(request, name):
    target = Difficulty.objects.filter(rating=name).first()
    if target is None:
        return render(request, ERROR_FILE)
    else:
        return render(request, DIFFICULTY_FILE, {
            'difficulties': Difficulty.objects.all(),
            'target': target
        })

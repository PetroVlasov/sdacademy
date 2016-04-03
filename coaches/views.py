from django.shortcuts import render
from coaches.models import Coach


def detail(request, item_id):
    coach = Coach.objects.get(id=item_id)
    return render(request, 'coaches/detail.html', {'coach': coach})

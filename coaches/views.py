from django.shortcuts import render
from coaches.models import Coach
from django.shortcuts import render_to_response

def detail(request, item_id):
    coach = Coach.objects.get(id=item_id)
    print coach.user.username
    return render(request, 'coaches/detail.html', {'coach': coach})

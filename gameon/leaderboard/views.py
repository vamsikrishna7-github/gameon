from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from play.models import UsersInfo
# Create your views here.
@login_required(login_url='login')
def leaderboard(r):
    data = UsersInfo.objects.all().order_by('-score')
    context = {
        'allusers': data,
        'n' : data.count()
    }
    return render(r, 'leaderboard.html', context)


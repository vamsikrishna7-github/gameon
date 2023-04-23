from django.shortcuts import render
from play.models import UsersInfo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def profile(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    context = {
        'userName': uinfo.userName,
        'email': uinfo.email,
        'level': uinfo.level,
        'score': uinfo.score
    }
    return render(r, 'profile.html', context)

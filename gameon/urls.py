"""gameon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from play import views as playviews
from Profile import views as profileviews
from contact import views as contactviews
from leaderboard import views as leaderboardviews
from about import views as aboutviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', playviews.login, name='login'),
    path('signup/', playviews.signup, name='signup'),
    path('home/', playviews.home, name='home'),
    path('profile/', profileviews.profile, name='profile'),
    path('contact/', contactviews.contact, name='contact'),
    path('leaderboard/', leaderboardviews.leaderboard, name='leaderboard'),
    path('about/', aboutviews.about, name='about'),
    path('logout/', playviews.Logout, name='logout'),
    path('levels/', playviews.levels, name='levels'),
    path('level1/', playviews.level1, name='level1'),
    path('level2/', playviews.level2, name='level2'),
    path('level3/', playviews.level3, name='level3'),
    path('level4/', playviews.level4, name='level4'),
    path('level5/', playviews.level5, name='level5'),
    path('level6/', playviews.level6, name='level6'),
    path('level7/', playviews.level7, name='level7'),
    path('level8/', playviews.level8, name='level8'),
    path('level9/', playviews.level9, name='level9'),
    path('level10/', playviews.level10, name='level10'),
]

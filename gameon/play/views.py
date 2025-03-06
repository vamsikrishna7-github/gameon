from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as Login
from django.contrib.auth.decorators import login_required
from play.models import UsersInfo
from .models import QuestionBank
import random
import json

@login_required(login_url='login')
def home(r):
    return render(r, 'index.html')

def login(r):
    if r.method=='POST':
        username=r.POST.get('username')
        pass1=r.POST.get('pass')
        user=authenticate(r,username=username,password=pass1)
        if user is not None:
            Login(r,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(r, 'login.html')

def signup(r):
    if r.method=='POST':
        uname=r.POST.get('username')
        email=r.POST.get('email')
        pass1=r.POST.get('password1')
        pass2=r.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        elif UsersInfo.objects.filter(userName=uname).exists():
            return HttpResponse("User name is already taken.")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()

            my_record = UsersInfo(userName =uname, email =email, password =pass1, level =0, score =0.0)
            my_record.save()

            return redirect('login')
        
    return render(r, 'signup.html')

@login_required(login_url='login')
def Logout(r):
    logout(r)
    return redirect('login')

@login_required(login_url='login')
def levels(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    context = {
        'userName': uinfo.userName,
        'level': uinfo.level + 1
    }
    return render(r, 'levels.html', context)

@login_required(login_url='login')
def level1(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 1:
        if r.method=='POST':
            if r.POST.get('option') == QuestionBank.objects.get(id=1).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 1:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level1.html', wrong)
        return render(r, 'level1.html',)
                
    wrong = {
        'errer1' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)


@login_required(login_url='login')
def level2(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 2:
        if r.method == 'POST':
            clicked_number_str = r.POST.get('number')
            if clicked_number_str.isdigit():
                clicked_number = int(clicked_number_str)
                expected_number = r.session.get('expected_number', 1)
                if clicked_number == expected_number:
                    r.session['expected_number'] = expected_number + 1
                    if expected_number == 25:
                        r.session.pop('expected_number')
                        uinfo.level +=1
                        uinfo.score +=100
                        uinfo.save()
                        return redirect('levels')
                    else:
                        x = json.loads(QuestionBank.objects.get(id=2).answer) 
                        x = {k: v for k, v in x.items() if v != clicked_number} #removing 
                        question_bank = QuestionBank.objects.get(id=2)
                        question_bank.answer = json.dumps(x)
                        question_bank.save()
                        return render(r, 'level2.html', x)
                else:
                    random_numbers = random.sample(range(1, 26), 25)
                    r.session['expected_number'] = 1
                    numbers_dict = {'number{}'.format(i+1): random_numbers[i] for i in range(len(random_numbers))}
                    x = QuestionBank.objects.get(id=2)
                    x.answer=json.dumps(numbers_dict)
                    x.save()
                    return render(r, 'level2.html', numbers_dict)
        else:
            random_numbers = random.sample(range(1, 26), 25)
            r.session['expected_number'] = 1
            numbers_dict = {'number{}'.format(i+1): random_numbers[i] for i in range(len(random_numbers))}
            x = QuestionBank.objects.get(id=2)
            x.answer=json.dumps(numbers_dict)
            x.save()
            return render(r, 'level2.html', numbers_dict)
    wrong = {
        'errer2' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)

@login_required(login_url='login')
def level3(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 3:
        if r.method=='POST':
            if r.POST.get('option') == QuestionBank.objects.get(id=3).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 3:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level3.html', wrong)
        return render(r, 'level3.html',)
                
    wrong = {
        'errer3' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)

@login_required(login_url='login')
def level4(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 4:
        if r.method=='POST':
            if r.POST.get('answer') == QuestionBank.objects.get(id=4).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 4:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level4.html', wrong)
        return render(r, 'level4.html',)
                
    wrong = {
        'errer4' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)

@login_required(login_url='login')
def level5(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 5:
        if r.method=='POST':
            if r.POST.get('answer') == QuestionBank.objects.get(id=5).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 4:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level5.html', wrong)
        return render(r, 'level5.html',)
                
    wrong = {
        'errer5' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)


@login_required(login_url='login')
def level6(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 6:
        if r.method=='POST':
            if r.POST.get('option') == QuestionBank.objects.get(id=6).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 1:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level6.html', wrong)
        return render(r, 'level6.html',)
                
    wrong = {
        'errer6' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)




@login_required(login_url='login')
def level7(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 7:
        if r.method=='POST':
            if r.POST.get('option') == QuestionBank.objects.get(id=7).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 1:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level7.html', wrong)
        return render(r, 'level7.html',)
                
    wrong = {
        'errer7' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)


@login_required(login_url='login')
def level8(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 8:
        if r.method=='POST':
            if r.POST.get('answer') == QuestionBank.objects.get(id=8).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 8:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level8.html', wrong)
        return render(r, 'level8.html',)
                
    wrong = {
        'errer8' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)


@login_required(login_url='login')
def level9(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 9:
        if r.method=='POST':
            if r.POST.get('answer') == QuestionBank.objects.get(id=9).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 9:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level9.html', wrong)
        return render(r, 'level9.html',)
                
    wrong = {
        'errer9' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)


@login_required(login_url='login')
def level10(r):
    uinfo = UsersInfo.objects.get(userName=r.user)
    if uinfo.level+1 == 10:
        if r.method=='POST':
            if r.POST.get('option') == QuestionBank.objects.get(id=10).answer:
                uinfo.level +=1
                uinfo.score +=100
                uinfo.save()
                return redirect('levels')
            else:
                if uinfo.level != 10:
                    uinfo.score -=25
                    uinfo.save()
                    wrong = {
                        'errer' : 'Wrong anser your score is -25'
                    }
                    return render(r, 'level10.html', wrong)
        return render(r, 'level10.html',)
                
    wrong = {
        'errer10' : 'Already completed!',
        'userName' : uinfo.userName,
        'level' : uinfo.level +1
    }
    return render(r, 'levels.html', wrong)
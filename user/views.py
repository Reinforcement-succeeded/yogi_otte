from django.shortcuts import render
from .models import CustomUser
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
symbol = '!@#$%^&*'
# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if not user:
            return render(request, 'user/signup.html')
        else:
            return redirect('/')

    elif request.method == 'POST':
        email = request.POST.get('useremail', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        username = request.POST.get('username', '')

        if email == '' or password == '' or password2 == '' or username == '':
            return render(request, 'user/signup.html', {'error':'빈칸은 허용되지 않는다'})
        else:
            if password != password2:
                return render(request, 'user/signup.html', {'error':'비밀번호 틀렸다 점검해라'})
            elif len(password) < 8:
                return render(request, 'user/signup.html', {'error':'비밀번호 8자리 이상으로 해라'})
            elif password.islower() != True:
                return render(request, 'user/signup.html', {'error':'소문자는 하나라도 포함되어 있어야지?'})
            elif any(i in symbol for i in password) != True:
                return render(request, 'user/signup.html', {'error':f'{symbol}중 하나가 포함되어야한다'})

            existUser = auth.get_user_model().objects.filter(email = email)
            if existUser:
                return render(request, 'user/signup.html', {'error':'이미 선점된 이메일이다.'})
            else:
                CustomUser.objects.create_user(
                    email=email,
                    password=password,
                    username=username
                )
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if not user:
            return render(request, 'user/signin.html')
        else:
            return redirect('/')

    elif request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(request, email=useremail, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': '존재하지 않는 메일이거나 비밀번호가 틀렸습니다.'})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
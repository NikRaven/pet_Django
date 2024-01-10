from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import UserTable
from .forms import UsersFrom, SignUpForm
from django_email_verification import send_email
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Add AuthenticationForm


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'for_users/login.html', {"form": form})


def users_home(request):
    news = UserTable.objects.order_by('-id')
    return render(request, 'for_users/users_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = UsersFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'
    form = UsersFrom()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'for_users/create.html', data)


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            # # высылаем письмо и делаем его неактивным
            # user.is_active = False
            # send_email(user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'for_users/signup.html', {'form': form})


# Create your views here.
def landing_page(request):
    return render(request, 'for_users/landing_page.html')

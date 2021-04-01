from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from user.models import User


def index(request):
    return render(request, 'index.html')


def login_end(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  # validating function
        if user is not None:
            login(request, user)
            if user.is_authenticated and user.is_teacher:
                messages.success(request, 'You are successfully logged in as Teacher!')
                return redirect('teacher_dashboard')
            else:
                return redirect('student_index')
        else:
            messages.error(request, 'Invalid Username or password!')
            return redirect('login')


def registration_view(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        cpass = request.POST['cpassword']
        if password == cpass:
            u1 = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_student=True
            )
            user = authenticate(username=username, password=password)  # validating function
            if user is not None:
                login(request, user)
                if user.is_authenticated:
                    return redirect('student_index')
            messages.error(request, '500 Internal server error')
            return redirect('register')
        else:
            messages.error(request, 'Passwords does not match')
            return redirect('register')


def logout_view(request):
    request.session.flush()
    logout(request)
    return HttpResponseRedirect('/')

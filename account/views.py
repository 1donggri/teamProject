from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return redirect("user:main")
        else:
            print("인증실패")
            return render(request, "account/login.html", {
                'error': 'ID 또는 Password가 일치하지 않습니다.',
            })

    return render(request, "account/login.html")

def logout_view(request):
    logout(request)

    return redirect("user:first")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("user:first")

    return render(request, "account/signup.html")

def main_view(request):
    template = loader.get_template('account/main.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def first_view(request):
    template = loader.get_template('account/first.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))